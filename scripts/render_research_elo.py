#!/usr/bin/env python3
"""Render the public portfolio data and the README ranking from GitHub issues."""

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

STATE = Path(".research-elo/ratings.json")
README = Path("README.md")
PUBLIC_DATA = Path("data/portfolio.json")
START = "<!-- RESEARCH_ELO_START -->"
END = "<!-- RESEARCH_ELO_END -->"


def api(path):
    request = urllib.request.Request(f"https://api.github.com{path}")
    request.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"GitHub API request failed ({error.code}): {detail}") from error


def open_ideas(repository):
    owner = repository.split("/", 1)[0].casefold()
    ideas = {}
    page = 1
    while True:
        batch = api(f"/repos/{repository}/issues?state=open&per_page=100&page={page}")
        if not batch:
            break
        for item in batch:
            if "pull_request" in item:
                continue
            if item.get("user", {}).get("login", "").casefold() != owner:
                continue
            if not item.get("title", "").startswith("[Idea]"):
                continue
            ideas[int(item["number"])] = item
        if len(batch) < 100:
            break
        page += 1
    return ideas


def atomic_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def build_rows(state, issues, repository):
    rows = []
    ratings = state.get("ratings", {})
    for number, issue in issues.items():
        score = ratings.get(str(number), {})
        rows.append(
            {
                "number": number,
                "title": issue["title"],
                "url": f"https://github.com/{repository}/issues/{number}",
                "rating": float(score.get("rating", 1500)),
                "games": int(score.get("games", 0)),
                "wins": int(score.get("wins", 0)),
                "draws": int(score.get("draws", 0)),
                "losses": int(score.get("losses", 0)),
                "updated_at": issue.get("updated_at"),
            }
        )
    rows.sort(key=lambda row: (row["games"] == 0, -row["rating"], row["number"]))
    return rows


def render_readme(readme, rows, generated_at):
    lines = [
        START,
        "### Current comparative ranking",
        "",
        "Ratings organize attention; the scientific reasoning and earliest decision-changing test matter more than small score differences.",
        "",
    ]
    if rows:
        lines.extend(
            [
                "| Rank | Research idea | Rating | Comparisons | Record |",
                "|---:|---|---:|---:|---:|",
            ]
        )
        ranked_index = 0
        for row in rows:
            title = row["title"].replace("|", "\\|")
            if row["games"]:
                ranked_index += 1
                rank = str(ranked_index)
                rating = f"**{row['rating']:.0f}**"
                record = f"{row['wins']}W / {row['draws']}D / {row['losses']}L"
            else:
                rank, rating, record = "—", "Awaiting comparison", "—"
            lines.append(
                f"| {rank} | [#{row['number']} — {title}]({row['url']}) | {rating} | {row['games']} | {record} |"
            )
    else:
        lines.append(
            "_No research ideas have been captured yet. Add two open `[Idea]` issues to begin pairwise comparison._"
        )
    lines.extend(["", f"_Last synchronized: {generated_at}._", END])
    section = "\n".join(lines)
    if START not in readme or END not in readme:
        raise RuntimeError("README ranking markers are missing.")
    start = readme.index(START)
    end = readme.index(END) + len(END)
    return readme[:start] + section + readme[end:]


def main():
    repository = os.environ["GITHUB_REPOSITORY"]
    state = json.loads(STATE.read_text(encoding="utf-8"))
    rows = build_rows(state, open_ideas(repository), repository)
    timestamp = datetime.now(timezone.utc)
    public = {
        "version": 1,
        "updated_at": timestamp.isoformat(),
        "ideas": rows,
    }
    atomic_text(PUBLIC_DATA, json.dumps(public, indent=2, ensure_ascii=False) + "\n")

    readme = README.read_text(encoding="utf-8")
    rendered = render_readme(readme, rows, timestamp.strftime("%Y-%m-%d %H:%M UTC"))
    atomic_text(README, rendered)


if __name__ == "__main__":
    main()
