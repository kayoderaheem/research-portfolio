# Research Portfolio

A structured workspace for capturing, evaluating, comparing, and developing research ideas before committing substantial research time.

The goal is to move from **interesting idea** to **testable scientific problem** and then make explicit decisions about whether to continue, pivot, park, or reject a direction.

## Research Elo

<!-- RESEARCH_ELO_START -->
_No research ideas have been rated yet. Create an issue whose title begins with `[Idea]` to start the portfolio._
<!-- RESEARCH_ELO_END -->

## Research workflow

Each research direction should begin as a GitHub Issue. The portfolio separates the scientific problem from the proposed method and asks what evidence would change our mind.

Suggested lifecycle:

`raw idea` → `literature check` → `feasibility` → `candidate` → `active` → `manuscript`

Alternative outcomes are equally useful:

`candidate` → `parked / rejected`

A rejected idea remains part of the scientific record because the reason it failed may inform later project selection.

## What every idea should answer

A strong research-idea issue should make the following explicit:

- **Observation:** What was noticed before an explanation was proposed?
- **Scientific problem:** What unresolved biological or computational problem does this expose?
- **Research question:** What is the precise question being asked?
- **Hypothesis:** What non-obvious claim could be supported or rejected?
- **Impact:** Why would answering the question matter?
- **Novelty:** What would be scientifically differentiated if the idea succeeds?
- **Prediction:** What should be observed if the hypothesis is correct, and what would argue against it?
- **Data readiness:** Which datasets can actually test the question?
- **Strong baselines:** What simpler or established methods must be beaten or matched?
- **Biggest assumption:** Which uncertain assumption is most likely to kill the project?
- **Cheapest discriminating test:** What is the earliest experiment or analysis that could change the decision?
- **Validation:** What independent evidence would make the result credible?
- **Go / No-Go criterion:** What result justifies continued investment?

## Automated comparative evaluation

Open owner-authored issues beginning with `[Idea]` are compared pairwise by an LLM judge. The resulting Elo-style scores are **decision aids, not measures of scientific truth or quality**.

The judge is instructed to compare ideas using:

1. scientific importance
2. clarity and falsifiability of the research question
3. novelty potential
4. tractability
5. data readiness
6. validation strength
7. leverage and reusability
8. publication potential

Ratings are most useful for exposing trade-offs and assumptions. Small numerical differences should not determine project choice.

## Recommended cadence

A useful default is:

`5 raw ideas` → `2 literature/feasibility checks` → `1 deep evaluation` → `1 cheapest discriminating experiment` → `continue / pivot / kill`

The portfolio should therefore record not only successful projects, but also failed assumptions, abandoned directions, and reasons for saying no.

## Principle

> Choose the scientific problem before optimizing the model.
