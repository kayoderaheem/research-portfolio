#!/usr/bin/env python3
"""Render a lightweight similarity map of open research ideas using only stdlib."""

import html
import json
import math
import os
import re
import urllib.request
from collections import Counter
from pathlib import Path

OUT = Path('docs/research_map.html')
MARKER = '<!-- research-idea-engine:v1 -->'
STOP = {
    'the','a','an','and','or','of','to','in','for','with','on','by','from','is','are','be','as','that','this',
    'can','could','will','would','do','does','using','use','research','idea','model','models','data','study','studies'
}


def api(path):
    req = urllib.request.Request(f'https://api.github.com{path}')
    req.add_header('Authorization', f"Bearer {os.environ['GITHUB_TOKEN']}")
    req.add_header('Accept', 'application/vnd.github+json')
    req.add_header('X-GitHub-Api-Version', '2022-11-28')
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode('utf-8'))


def ideas():
    repo = os.environ['GITHUB_REPOSITORY']
    owner = repo.split('/', 1)[0].casefold()
    result = []
    page = 1
    while True:
        batch = api(f'/repos/{repo}/issues?state=open&per_page=100&page={page}')
        if not batch:
            break
        for issue in batch:
            if 'pull_request' in issue or not issue.get('title', '').startswith('[Idea]'):
                continue
            author = issue.get('user', {}).get('login', '').casefold()
            if author != owner and MARKER not in (issue.get('body') or ''):
                continue
            result.append(issue)
        if len(batch) < 100:
            break
        page += 1
    return result


def tokens(text):
    words = re.findall(r'[A-Za-z][A-Za-z0-9+-]{2,}', text.lower())
    return [w for w in words if w not in STOP]


def tfidf_vectors(items):
    docs = [Counter(tokens((x.get('title') or '') + ' ' + (x.get('body') or ''))) for x in items]
    df = Counter()
    for doc in docs:
        for term in doc:
            df[term] += 1
    n = max(len(docs), 1)
    vecs = []
    for doc in docs:
        vec = {}
        for term, count in doc.items():
            vec[term] = (1 + math.log(count)) * math.log((n + 1) / (df[term] + 1))
        norm = math.sqrt(sum(v*v for v in vec.values())) or 1.0
        vecs.append({k: v / norm for k, v in vec.items()})
    return vecs


def cosine(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(v * b.get(k, 0.0) for k, v in a.items())


def coordinates(vecs):
    n = len(vecs)
    if n == 0:
        return []
    coords = []
    radius = 260
    for i in range(n):
        angle = 2 * math.pi * i / max(n, 1)
        coords.append([400 + radius * math.cos(angle), 330 + radius * math.sin(angle)])
    # Pull similar ideas toward one another; deterministic and dependency-free.
    for _ in range(80):
        updated = []
        for i, (x, y) in enumerate(coords):
            fx = fy = 0.0
            for j, (x2, y2) in enumerate(coords):
                if i == j:
                    continue
                dx, dy = x2 - x, y2 - y
                d2 = dx*dx + dy*dy + 1.0
                sim = cosine(vecs[i], vecs[j])
                if sim > 0.08:
                    fx += dx * sim * 0.002
                    fy += dy * sim * 0.002
                if d2 < 14000:
                    fx -= dx / d2 * 120
                    fy -= dy / d2 * 120
            updated.append([min(760,max(40,x+fx)), min(620,max(40,y+fy))])
        coords = updated
    return coords


def render(items):
    repo = os.environ['GITHUB_REPOSITORY']
    vecs = tfidf_vectors(items)
    coords = coordinates(vecs)
    edges = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            sim = cosine(vecs[i], vecs[j])
            if sim >= 0.18:
                edges.append((i, j, sim))

    svg_edges = []
    for i, j, sim in sorted(edges, key=lambda x: -x[2])[:120]:
        x1, y1 = coords[i]; x2, y2 = coords[j]
        opacity = min(0.75, 0.15 + sim)
        width = 0.8 + 3 * sim
        svg_edges.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#94a3b8" stroke-opacity="{opacity:.2f}" stroke-width="{width:.1f}"/>')

    nodes = []
    cards = []
    for idx, issue in enumerate(items):
        x, y = coords[idx]
        num = int(issue['number'])
        raw_title = issue.get('title', '').replace('[Idea]', '').strip()
        title = html.escape(raw_title)
        url = f'https://github.com/{repo}/issues/{num}'
        nodes.append(
            f'<a href="{url}"><circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="#2563eb"/>'
            f'<text x="{x+17:.1f}" y="{y+4:.1f}" font-size="12" fill="#0f172a">#{num}</text></a>'
        )
        cards.append(f'<li><a href="{url}">#{num} — {title}</a></li>')

    document = f'''<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Research Idea Map</title>
<style>body{{font-family:system-ui,-apple-system,sans-serif;margin:0;background:#f8fafc;color:#0f172a}}main{{max-width:1050px;margin:auto;padding:28px}}.panel{{background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px;margin-bottom:22px}}svg{{width:100%;height:auto}}a{{color:#1d4ed8;text-decoration:none}}li{{margin:8px 0}}.note{{color:#475569}}</style></head>
<body><main><h1>Research Idea Map</h1><p class="note">Open ideas are positioned by text similarity from their titles and issue bodies. Connections indicate lexical/semantic overlap and are organizational aids, not measures of scientific quality.</p>
<div class="panel"><svg viewBox="0 0 800 660" role="img" aria-label="Research idea similarity map">{''.join(svg_edges)}{''.join(nodes)}</svg></div>
<div class="panel"><h2>Open ideas</h2><ol>{''.join(cards)}</ol></div>
</main></body></html>'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(document, encoding='utf-8')


if __name__ == '__main__':
    render(ideas())
