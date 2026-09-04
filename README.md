# Research Portfolio

An automated research-problem discovery and decision system for computational biology and precision medicine.

Every day, this repository scans recent Europe PMC and arXiv records, asks GitHub Copilot to propose a small set of evidence-linked research directions, checks the result against strict scientific and safety rules, and publishes up to three `[Idea]` issues for human review. It keeps a ledger so the same papers and ideas are not repeatedly proposed.

The organizing intuition comes from Michael A. Fischbach's 2024 *Cell* commentary, ["Problem choice and decision trees in science and engineering"](https://doi.org/10.1016/j.cell.2024.03.012). This is an independent bioinformatics adaptation, not an official implementation or affiliation.

## What the automation does

```text
Weekly schedule or manual run
             │
             ▼
 Europe PMC + arXiv scan
             │
             ▼
 Remove previously seen and duplicate papers
             │
             ▼
 GitHub Copilot proposes structured candidates
        (read-only job)
             │
             ▼
 Deterministic scientific and citation checks
             │
             ▼
 Separate publisher creates 0–3 labeled issues
             │
             ▼
 Persistent ledger prevents repetition
```

The scan rotates through four editable focus areas:

- cancer drug response and resistance;
- single-cell and spatial treatment response;
- multimodal precision medicine;
- perturbation models and virtual cells.

Each published issue includes the observation, scientific problem, falsifiable question, hypothesis and competing explanation, impact function, fixed anchor, floating parameters, scientific and technical assumptions, data and leakage plan, strong baselines, validation plan, an early discriminating test, and positive/ambiguous/negative branches.

## Use it

### Automatic weekly use

Once GitHub Copilot is available to Actions for the repository owner, no routine action is required. [`Generate Research Ideas`](.github/workflows/generate-research-ideas.yml) runs every day at 14:17 UTC. If fewer than four new eligible sources are found, it publishes nothing rather than manufacture a weak idea.

### Run it now or choose a topic

1. Open the repository's **Actions** tab.
2. Select **Generate Research Ideas**.
3. Choose **Run workflow**.
4. Optionally enter a focus such as `spatial transcriptomics treatment resistance` and choose a 7-, 14-, or 30-day lookback.

The workflow creates public GitHub issues labeled `research-idea`, `ai-generated`, and `needs-human-review`. Review an idea before committing resources; automation proposes candidates, not scientific truth.

### Change what it studies

Edit [`config/research-focus.json`](config/research-focus.json). Each focus area has:

- a plain-language name;
- search terms used by Europe PMC and arXiv;
- priority questions that guide proposal generation.

Changes are checked automatically before they reach the default branch.

## How quality is protected

The workflow follows a least-privilege publishing design:

1. The Copilot job can read sources and existing issue titles but cannot create issues or change repository files.
2. Its output must be strict structured data. A regular Python checker rejects unknown citations, repeated ideas, missing fields, weak assumption maps, missing independent validation, invalid time ranges, and out-of-range scores.
3. Only a separate publishing job receives issue-writing permission, and it can create no more than three candidates per run.
4. Source links in issues come from the trusted literature bundle, not from text invented by the model.
5. The ledger at [`.research-ideas/ledger.json`](.research-ideas/ledger.json) records reviewed sources and generated ideas.

The bioinformatics checks explicitly require patient- or donor-level independence where applicable, leakage-resistant preprocessing and evaluation, strong simple and established baselines, uncertainty and calibration when relevant, external or orthogonal validation, and cautious treatment of retrospective clinical claims.

## Compare promising ideas

The optional [`Research Problem-Choice Review`](.github/workflows/research-elo.yml) compares two or more open `[Idea]` issues. Run it manually with an issue number after reviewing the generated candidates. It identifies the stronger current investment, the main assumption that could reverse that choice, and the cheapest next test. Ratings organize attention; they do not establish novelty, truth, or clinical value.

<!-- RESEARCH_ELO_START -->
### Current comparative ranking

Ratings organize attention; the scientific reasoning and earliest decision-changing test matter more than small score differences.

_No research ideas have been captured yet. Add two open `[Idea]` issues to begin pairwise comparison._

_Last synchronized: not yet._
<!-- RESEARCH_ELO_END -->

## Add ideas manually

Automation and human judgment can coexist. Use either issue form:

- [Quick Research Idea](https://github.com/kayoderaheem/research-portfolio/issues/new?template=quick-research-idea.yml) for an early question.
- [Deep Evaluation](https://github.com/kayoderaheem/research-portfolio/issues/new?template=deep-evaluation.yml) for a project approaching commitment.

Keep the `[Idea]` prefix. Owner-authored issues and validated automated issues are eligible for comparison.

## The adapted problem-choice framework

The system makes six practices concrete:

1. **Generate in parallel.** Compare several important problems before committing.
2. **Name the optimization function.** Decide what impact means for the project.
3. **Fix one anchor.** Hold the scientific goal or unique capability fixed and let models, datasets, cohorts, assays, and modalities float.
4. **Map assumptions.** Separate scientific-reality assumptions from technical-capability assumptions and record time-to-readout.
5. **Test the weakest link early.** Run the cheapest experiment that can genuinely change the decision.
6. **Keep every branch useful.** Define what to do after positive, ambiguous, and negative results, and preserve residual learning if the favored hypothesis fails.

See [the full adaptation notes](docs/framework.md) and the [`drug-response/`](drug-response/) workspace for reusable paper and idea cards.

## Run the checks locally

No Python packages are required.

```bash
python -m unittest discover -s tests -v
python -m py_compile scripts/*.py
python -m json.tool config/research-focus.json >/dev/null
```

The automation itself runs in GitHub Actions and installs the official GitHub Copilot CLI during a run. The repository owner must have Copilot access that permits Copilot requests from Actions. No long-lived personal access token is stored.

## Responsible use

- Treat every generated item as a candidate for expert challenge, not a recommendation to begin a study.
- Verify novelty with a documented literature review before making novelty claims.
- Never place patient identifiers, protected health information, unpublished sensitive data, credentials, or access tokens in public issues or configuration.
- Pre-register decisive endpoints, data exclusions, and validation rules when appropriate.
- Preserve negative results and reasons for stopping; they are part of the research record.
- Do not use the scores or rankings to evaluate people.

## Design references

- Fischbach MA. [Problem choice and decision trees in science and engineering](https://doi.org/10.1016/j.cell.2024.03.012). *Cell*. 2024;187(8):1828–1833.
- Stanford Engineering. [How to pick—and solve—the next great problem](https://engineering.stanford.edu/news/how-pick-and-solve-next-great-problem).
- GitHub. [Using GitHub Copilot CLI in GitHub Actions](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions).
- GitHub Agentic Workflows. [Creating workflows](https://github.github.com/gh-aw/setup/creating-workflows/) and [safe outputs](https://github.github.com/gh-aw/reference/safe-outputs/).
- GitHub Next. [Weekly research workflow example](https://github.com/githubnext/agentics/blob/main/workflows/weekly-research.md).
- GitHub. [Daily arXiv researcher example](https://github.com/github/gh-aw/blob/main/.github/workflows/daily-arxiv-researcher.md).

## License

Repository code and original documentation are available under the [MIT License](LICENSE). Cited works remain the property of their respective rights holders.
