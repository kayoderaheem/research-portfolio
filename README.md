# Research Portfolio

A public problem-choice system for computational biology and precision medicine.

**Live site:** `https://kayoderaheem.github.io/research-portfolio/`

This repository helps a researcher spend more time choosing a consequential scientific problem before spending months or years optimizing a solution. It turns early intuition into an explicit, reviewable record of impact, assumptions, risk, evidence, and possible pivots.

## What this is

The repository combines three things:

1. **A public portfolio website** that explains the framework and displays current research ideas.
2. **Structured GitHub Issue templates** for capturing quick ideas and conducting deep evaluations.
3. **A comparative review workflow** that contrasts mature ideas, records the main risk and next discriminating test, and updates the public portfolio.

The organizing intuition comes from Michael A. Fischbach's 2024 *Cell* commentary, ["Problem choice and decision trees in science and engineering"](https://doi.org/10.1016/j.cell.2024.03.012). This is an independent bioinformatics adaptation, not an official implementation or affiliation.

## Start in three steps

### 1. Capture at least two candidate problems

Use either issue form:

- [Quick Research Idea](https://github.com/kayoderaheem/research-portfolio/issues/new?template=quick-research-idea.yml) for an early question.
- [Deep Evaluation](https://github.com/kayoderaheem/research-portfolio/issues/new?template=deep-evaluation.yml) for a project approaching commitment.

Keep the automatic `[Idea]` prefix in the issue title. Only open ideas created by the repository owner enter the portfolio.

### 2. Let the comparison run

Opening, editing, or reopening an owner-authored `[Idea]` issue starts the workflow. The first idea is published but not scored. Once a second idea exists, the workflow compares the target with relevant open candidates.

The review considers:

- scientific or translational impact;
- question quality and falsifiability;
- the chain of scientific and technical assumptions;
- time until high-risk assumptions can be tested;
- novelty and competitive advantage;
- flexibility about methods, cohorts, assays, and modalities;
- leakage-resistant validation, strong baselines, calibration, uncertainty, and independent evidence;
- the earliest result that should trigger continue, refine, pivot, park, or stop.

### 3. Read the reasoning, not just the score

The workflow posts a structured review on the idea and updates the table below. Elo-style ratings are comparative decision aids. They are not measures of scientific truth, novelty, or publication certainty.

## Research Elo

<!-- RESEARCH_ELO_START -->
### Current comparative ranking

Ratings organize attention; the scientific reasoning and earliest decision-changing test matter more than small score differences.

_No research ideas have been captured yet. Add two open `[Idea]` issues to begin pairwise comparison._

_Last synchronized: not yet._
<!-- RESEARCH_ELO_END -->

## The adapted framework

The workflow makes six practices concrete:

1. **Generate in parallel.** Develop and compare several candidate problems before committing.
2. **Name the optimization function.** Decide what impact means for this project.
3. **Fix one anchor.** Hold the scientific goal or unique capability fixed and let other parameters float.
4. **Map assumptions.** Score scientific reality and technical capability separately by risk and time-to-readout.
5. **Test the weakest link early.** Run the cheapest experiment that can genuinely change the decision.
6. **Revisit the decision tree.** Alternate focused execution with detached critical review and use failure to find a stronger branch.

See [the full adaptation notes](docs/framework.md) for the mapping to computational biology and precision medicine.

## Current domain workspace

The [`drug-response/`](drug-response/) workspace tracks questions in cancer drug response, perturbation biology, multimodal modeling, and treatment-response translation. Paper cards collect reusable scientific information; idea cards convert that information into testable projects.

## Website maintenance

The website is dependency-free HTML, CSS, and JavaScript. Its live idea cards are generated in `data/portfolio.json` whenever the review workflow runs.

To preview locally:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

To run the checks:

```bash
python -m unittest discover -s tests -v
```

## Automation requirements

The review uses GitHub Copilot CLI inside GitHub Actions. The repository owner's GitHub account must have Copilot access that permits Copilot requests from Actions. The workflow uses GitHub's short-lived built-in token; no long-lived secret is stored by default.

If Copilot access is unavailable, the website and idea templates still work. The comparison job will show a clear failure in the Actions tab instead of silently publishing an incomplete rating.

## Responsible use

- Treat automated comparisons as prompts for expert discussion.
- Verify novelty through a documented literature review.
- Never place patient identifiers, protected health information, unpublished sensitive data, credentials, or access tokens in public issues.
- Pre-register decisive endpoints and validation rules when appropriate.
- Preserve negative results and reasons for stopping; they are part of the research record.
- Do not use portfolio ratings to evaluate people.

## Sources

- Fischbach MA. [Problem choice and decision trees in science and engineering](https://doi.org/10.1016/j.cell.2024.03.012). *Cell*. 2024;187(8):1828-1833.
- Stanford Engineering. [How to pick - and solve - the next great problem](https://engineering.stanford.edu/news/how-pick-and-solve-next-great-problem).

## License

Repository code and original documentation are available under the [MIT License](LICENSE). The cited paper and its figures remain the property of their respective rights holders; no paper figures are reproduced here.
