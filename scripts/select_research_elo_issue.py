#!/usr/bin/env python3
"""Select an open research idea that most needs another pairwise comparison."""

import json
import os
import urllib.request
from pathlib import Path

STATE = Path('.research-elo/ratings.json')
MARKER = '<!-- research-idea-engine:v1 -->'


def api(path):
    req = urllib.request.Request(f'https://api.github.com{path}')
    req.add_header('Authorization', f"Bearer {os.environ['GITHUB_TOKEN']}")
    req.add_header('Accept', 'application/vnd.github+json')
    req.add_header('X-GitHub-Api-Version', '2022-11-28')
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode('utf-8'))


def open_ideas():
    repo = os.environ['GITHUB_REPOSITORY']
    owner = repo.split('/', 1)[0].casefold()
    ideas = []
    page = 1
    while True:
        batch = api(f'/repos/{repo}/issues?state=open&per_page=100&page={page}')
        if not batch:
            break
        for item in batch:
            if 'pull_request' in item:
                continue
            if not item.get('title', '').startswith('[Idea]'):
                continue
            author = item.get('user', {}).get('login', '').casefold()
            if author != owner and MARKER not in (item.get('body') or ''):
                continue
            ideas.append(item)
        if len(batch) < 100:
            break
        page += 1
    return ideas


def main():
    ideas = open_ideas()
    if not ideas:
        raise SystemExit('No eligible open [Idea] issues found.')
    state = json.loads(STATE.read_text()) if STATE.exists() else {'ratings': {}}
    ratings = state.get('ratings', {})

    def key(issue):
        entry = ratings.get(str(issue['number']), {})
        games = int(entry.get('games', 0))
        rating = float(entry.get('rating', 1500))
        return (games, abs(rating - 1500), int(issue['number']))

    chosen = min(ideas, key=key)
    print(chosen['number'])


if __name__ == '__main__':
    main()
