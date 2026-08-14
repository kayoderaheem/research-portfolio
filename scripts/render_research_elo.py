#!/usr/bin/env python3

import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

STATE = Path('.research-elo/ratings.json')
README = Path('README.md')
START = '<!-- RESEARCH_ELO_START -->'
END = '<!-- RESEARCH_ELO_END -->'


def api(path):
    req = urllib.request.Request(f'https://api.github.com{path}')
    req.add_header('Authorization', f'Bearer {os.environ["GITHUB_TOKEN"]}')
    req.add_header('Accept', 'application/vnd.github+json')
    req.add_header('X-GitHub-Api-Version', '2022-11-28')
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def open_ideas(repo):
    owner = repo.split('/')[0]
    out = {}
    page = 1
    while True:
        batch = api(f'/repos/{repo}/issues?state=open&per_page=100&page={page}')
        if not batch:
            break
        for item in batch:
            if 'pull_request' in item:
                continue
            if item.get('user', {}).get('login') != owner:
                continue
            if not item.get('title', '').startswith('[Idea]'):
                continue
            out[int(item['number'])] = item
        if len(batch) < 100:
            break
        page += 1
    return out


def main():
    repo = os.environ['GITHUB_REPOSITORY']
    state = json.loads(STATE.read_text())
    issues = open_ideas(repo)
    rows = []
    for key, score in state.get('ratings', {}).items():
        number = int(key)
        if number in issues:
            rows.append((number, score, issues[number]))
    rows.sort(key=lambda x: (-float(x[1].get('rating', 1500)), x[0]))

    lines = [START, '### Current comparative ranking', '', 'Ratings are comparative LLM feedback. The scientific reasoning behind each comparison matters more than small Elo differences.', '']
    if rows:
        lines += ['| Rank | Research idea | Elo | Games | Record |', '|---:|---|---:|---:|---:|']
        for rank, (number, score, issue) in enumerate(rows, 1):
            title = issue['title'].replace('|', '\\|')
            url = f'https://github.com/{repo}/issues/{number}'
            lines.append(f'| {rank} | [#{number} — {title}]({url}) | **{float(score.get("rating",1500)):.0f}** | {score.get("games",0)} | {score.get("wins",0)}W / {score.get("draws",0)}D / {score.get("losses",0)}L |')
    else:
        lines.append('_No research ideas have been rated yet. At least two open `[Idea]` issues are needed for pairwise comparison._')
    lines += ['', f'_Last rendered: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}._', END]
    section = '\n'.join(lines)

    readme = README.read_text()
    start = readme.index(START)
    end = readme.index(END) + len(END)
    README.write_text(readme[:start] + section + readme[end:])


if __name__ == '__main__':
    main()
