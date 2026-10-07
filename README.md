# Research Portfolio

An automated research-problem discovery and decision system for computational biology and precision medicine.

Every day, this repository scans major open scholarly, biomedical, preprint, clinical-trial, and functional-genomics databases; asks GitHub Copilot to propose a small set of evidence-linked research directions; checks the result against strict scientific and safety rules; and publishes up to three `[Idea]` issues for human review. It keeps a ledger so the same records and ideas are not repeatedly proposed.

The organizing intuition comes from Michael A. Fischbach's 2024 *Cell* commentary, ["Problem choice and decision trees in science and engineering"](https://doi.org/10.1016/j.cell.2024.03.012). This is an independent bioinformatics adaptation, not an official implementation or affiliation.

## What the automation does

```text
Weekly schedule or manual run
             │
             ▼
 Multi-database evidence scan
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

### Database coverage

The default scan connects to:

- **Europe PMC**, including PubMed and other biomedical feeds;
- **arXiv** for quantitative-biology and computational preprints;
- **OpenAlex** for broad cross-disciplinary scholarship;
- **Crossref** for publisher-deposited DOI records;
- **Semantic Scholar** for semantic scholarly search;
- **bioRxiv and medRxiv** for biology and health-science preprints;
- **ClinicalTrials.gov** for registered studies;
- **NCBI GEO** for public functional-genomics datasets.

Results are deduplicated across databases by DOI, accession, identifier, and title similarity. The final evidence bundle is balanced across sources so a large general index cannot displace specialist trial or dataset records. Closed databases such as Scopus, Web of Science, and subscription-only resources require separate licenses and credentials and therefore cannot be queried anonymously.

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
- search terms used across the connected databases;
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

| Rank | Research idea | Rating | Comparisons | Record |
|---:|---|---:|---:|---:|
| 1 | [#33 — [Idea] Identifiability limits of conserved and context-specific drug responses](https://github.com/kayoderaheem/research-portfolio/issues/33) | **1641** | 15 | 14W / 0D / 1L |
| 2 | [#30 — [Idea] Population-calibrated multimodal prediction of thiopurine toxicity](https://github.com/kayoderaheem/research-portfolio/issues/30) | **1638** | 15 | 14W / 0D / 1L |
| 3 | [#28 — [Idea] Incremental decision value and cross-registry calibration of blood-based T2 biomarkers for asthma exacerbation risk](https://github.com/kayoderaheem/research-portfolio/issues/28) | **1611** | 20 | 15W / 0D / 5L |
| 4 | [#42 — [Idea] Longitudinal MRD-state signatures that distinguish response from refractory escape in multiple myeloma](https://github.com/kayoderaheem/research-portfolio/issues/42) | **1594** | 16 | 12W / 0D / 4L |
| 5 | [#24 — [Idea] External calibration of multimodal HCC surveillance triage](https://github.com/kayoderaheem/research-portfolio/issues/24) | **1594** | 21 | 14W / 1D / 6L |
| 6 | [#48 — [Idea] Cross-assay reproducibility of functional drug-sensitivity rankings from clinical tumor samples](https://github.com/kayoderaheem/research-portfolio/issues/48) | **1592** | 10 | 9W / 0D / 1L |
| 7 | [#36 — [Idea] Reference-invariant identification of direct perturbation effects in single-cell models](https://github.com/kayoderaheem/research-portfolio/issues/36) | **1589** | 14 | 11W / 0D / 3L |
| 8 | [#25 — [Idea] Treatment-specific multimodal validation of lupus nephritis response programs](https://github.com/kayoderaheem/research-portfolio/issues/25) | **1575** | 23 | 14W / 1D / 8L |
| 9 | [#31 — [Idea] Site-transportable multimodal validation of corneal nerve imaging for small-fiber neuropathy](https://github.com/kayoderaheem/research-portfolio/issues/31) | **1564** | 24 | 15W / 0D / 9L |
| 10 | [#17 — [Idea] Patient-level tissue-context gain over composition for multimodal lymphoma treatment-response prediction](https://github.com/kayoderaheem/research-portfolio/issues/17) | **1563** | 20 | 13W / 0D / 7L |
| 11 | [#51 — [Idea] Transportable kinase-activity states for predicting drug response across tumor cohorts](https://github.com/kayoderaheem/research-portfolio/issues/51) | **1557** | 5 | 5W / 0D / 0L |
| 12 | [#60 — [Idea] Spatial cGAS–STING–fibrosis boundaries that determine combined TACE–checkpoint response](https://github.com/kayoderaheem/research-portfolio/issues/60) | **1556** | 5 | 5W / 0D / 0L |
| 13 | [#56 — [Idea] Exposure-normalized mechanisms of HER2 antibody-drug-conjugate sensitivity and resistance](https://github.com/kayoderaheem/research-portfolio/issues/56) | **1549** | 8 | 6W / 0D / 2L |
| 14 | [#39 — [Idea] Composition-aware counterfactuals for unseen perturbations across tissue neighborhoods](https://github.com/kayoderaheem/research-portfolio/issues/39) | **1544** | 18 | 11W / 0D / 7L |
| 15 | [#43 — [Idea] Transportability limits of multimodal drug-response prediction under unseen-drug and unseen-tumor shifts](https://github.com/kayoderaheem/research-portfolio/issues/43) | **1540** | 20 | 12W / 0D / 8L |
| 16 | [#45 — [Idea] Incremental treatment-decision value of functional drug screening beyond genomic matching in pediatric brain tumors](https://github.com/kayoderaheem/research-portfolio/issues/45) | **1536** | 9 | 6W / 0D / 3L |
| 17 | [#1 — [Idea] Time-to-decision functional profiling for resistance-aware combination therapy](https://github.com/kayoderaheem/research-portfolio/issues/1) | **1529** | 30 | 16W / 0D / 14L |
| 18 | [#27 — [Idea] Decision-value and site-transportable calibration of temporal multimodal deterioration risk in ICU care](https://github.com/kayoderaheem/research-portfolio/issues/27) | **1526** | 26 | 14W / 0D / 12L |
| 19 | [#40 — [Idea] Context-aware virtual screening of apoptosis combinations in germ cell tumors](https://github.com/kayoderaheem/research-portfolio/issues/40) | **1524** | 25 | 13W / 1D / 11L |
| 20 | [#53 — [Idea] Early treatment-decision value of heterogeneity trajectories in HER2-targeted bladder cancer](https://github.com/kayoderaheem/research-portfolio/issues/53) | **1522** | 6 | 4W / 0D / 2L |
| 21 | [#55 — [Idea] Mutation-specific target engagement as a separator of intrinsic sensitivity and resistance](https://github.com/kayoderaheem/research-portfolio/issues/55) | **1522** | 8 | 5W / 0D / 3L |
| 22 | [#54 — [Idea] Persistence and specificity of treatment-induced T-cell clones as a response discriminator in checkpoint therapy](https://github.com/kayoderaheem/research-portfolio/issues/54) | **1522** | 10 | 6W / 0D / 4L |
| 23 | [#61 — [Idea] Spatially resolved IGF2BP3–MHC-I competence as an incremental checkpoint-response predictor in triple-negative breast cancer](https://github.com/kayoderaheem/research-portfolio/issues/61) | **1520** | 6 | 4W / 0D / 2L |
| 24 | [#50 — [Idea] Population-calibrated pharmacogenomic prediction of tamoxifen benefit and endocrine resistance](https://github.com/kayoderaheem/research-portfolio/issues/50) | **1520** | 6 | 4W / 0D / 2L |
| 25 | [#15 — [Idea] BMP-restraint failure and BCL2-high niches as predictors of diffuse gastric cancer treatment response](https://github.com/kayoderaheem/research-portfolio/issues/15) | **1518** | 24 | 12W / 1D / 11L |
| 26 | [#13 — [Idea] Spatial CAF–immune buffering of EGFR-targeted therapy in lung adenocarcinoma](https://github.com/kayoderaheem/research-portfolio/issues/13) | **1518** | 25 | 13W / 0D / 12L |
| 27 | [#2 — [Idea] Transportable response signatures for molecularly matched therapy in advanced pancreatic cancer](https://github.com/kayoderaheem/research-portfolio/issues/2) | **1518** | 26 | 14W / 0D / 12L |
| 28 | [#11 — [Idea] Spatially constrained T-cell fitness states predicting blinatumomab response in B-cell leukemia](https://github.com/kayoderaheem/research-portfolio/issues/11) | **1506** | 23 | 11W / 1D / 11L |
| 29 | [#57 — [Idea] Pre-existing stromal architecture as an incremental predictor of bispecific-antibody response](https://github.com/kayoderaheem/research-portfolio/issues/57) | **1504** | 8 | 4W / 0D / 4L |
| 30 | [#7 — [Idea] Reproducible adaptive cell-state transitions after KRAS pathway blockade](https://github.com/kayoderaheem/research-portfolio/issues/7) | **1492** | 33 | 16W / 0D / 17L |
| 31 | [#49 — [Idea] Exposure-adjusted phosphoproteomic signatures of pharmacologic failure versus biological resistance](https://github.com/kayoderaheem/research-portfolio/issues/49) | **1486** | 11 | 5W / 0D / 6L |
| 32 | [#41 — [Idea] Falsifying resettable virtual-cell models of quiescent chromatin](https://github.com/kayoderaheem/research-portfolio/issues/41) | **1478** | 20 | 9W / 0D / 11L |
| 33 | [#59 — [Idea] Spatial access states that determine engineered T-cell treatment response](https://github.com/kayoderaheem/research-portfolio/issues/59) | **1477** | 6 | 2W / 0D / 4L |
| 34 | [#9 — [Idea] Spatially resolved IL-17 and retinoid states predicting tunnel-directed therapy response in hidradenitis suppurativa](https://github.com/kayoderaheem/research-portfolio/issues/9) | **1477** | 25 | 11W / 1D / 13L |
| 35 | [#18 — [Idea] Spatially resolved metabolic-inflammatory routes to gemcitabine resistance in cholangiocarcinoma](https://github.com/kayoderaheem/research-portfolio/issues/18) | **1477** | 27 | 12W / 1D / 14L |
| 36 | [#62 — [Idea] Reproducible tumor–lung interface ERK adaptation after MCL1 inhibition](https://github.com/kayoderaheem/research-portfolio/issues/62) | **1476** | 2 | 0W / 0D / 2L |
| 37 | [#10 — [Idea] Metabolite-defined resident-memory niches that determine checkpoint response in hepatocellular carcinoma](https://github.com/kayoderaheem/research-portfolio/issues/10) | **1468** | 27 | 12W / 0D / 15L |
| 38 | [#52 — [Idea] Isoform-switching mechanisms that separate intrinsic from acquired drug resistance](https://github.com/kayoderaheem/research-portfolio/issues/52) | **1464** | 7 | 2W / 0D / 5L |
| 39 | [#8 — [Idea] Metastatic-site spatial niches that modify ALK-inhibitor response](https://github.com/kayoderaheem/research-portfolio/issues/8) | **1463** | 23 | 10W / 0D / 13L |
| 40 | [#4 — [Idea] Reproducible myeloid-niche remodeling as a determinant of metastatic immunotherapy response](https://github.com/kayoderaheem/research-portfolio/issues/4) | **1462** | 26 | 11W / 1D / 14L |
| 41 | [#26 — [Idea] Site-robust multimodal risk stratification for fetal growth restriction management](https://github.com/kayoderaheem/research-portfolio/issues/26) | **1461** | 23 | 10W / 0D / 13L |
| 42 | [#34 — [Idea] Prospective falsification of a dynamic proteomic virtual cell across unseen therapies and organoid contexts](https://github.com/kayoderaheem/research-portfolio/issues/34) | **1461** | 17 | 7W / 0D / 10L |
| 43 | [#38 — [Idea] Cross-species identifiability of conserved versus context-specific perturbation responses](https://github.com/kayoderaheem/research-portfolio/issues/38) | **1460** | 14 | 5W / 0D / 9L |
| 44 | [#5 — [Idea] Spatially resolved immune-priming trajectories during cervical chemoradiotherapy](https://github.com/kayoderaheem/research-portfolio/issues/5) | **1460** | 20 | 7W / 3D / 10L |
| 45 | [#35 — [Idea] Causal transfer of chromatin-to-expression perturbation models across ATRX-deficient sarcoma states](https://github.com/kayoderaheem/research-portfolio/issues/35) | **1459** | 16 | 6W / 0D / 10L |
| 46 | [#23 — [Idea] Incremental value of dynamic inflammation for recovery-guided rehabilitation after knee arthroplasty](https://github.com/kayoderaheem/research-portfolio/issues/23) | **1458** | 28 | 12W / 0D / 16L |
| 47 | [#46 — [Idea] TET2-mutant clonal-hematopoiesis macrophages as a reversible cause of BRAF/MEK resistance in anaplastic thyroid cancer](https://github.com/kayoderaheem/research-portfolio/issues/46) | **1457** | 7 | 1W / 1D / 5L |
| 48 | [#44 — [Idea] Early functional detection of hypoxia-mediated resistance before radiographic treatment failure](https://github.com/kayoderaheem/research-portfolio/issues/44) | **1456** | 20 | 8W / 0D / 12L |
| 49 | [#3 — [Idea] Early detection of DNA-damage-tolerance escape during genotoxic therapy](https://github.com/kayoderaheem/research-portfolio/issues/3) | **1454** | 24 | 10W / 0D / 14L |
| 50 | [#47 — [Idea] Cross-cancer validation of lactate-transport states as predictors of drug-tolerant persistence](https://github.com/kayoderaheem/research-portfolio/issues/47) | **1453** | 8 | 2W / 0D / 6L |
| 51 | [#37 — [Idea] Prospective falsification of multimodal virtual-cell predictions for regulatory-state perturbations](https://github.com/kayoderaheem/research-portfolio/issues/37) | **1442** | 19 | 7W / 0D / 12L |
| 52 | [#32 — [Idea] Clinical-use validation of multimodal myocarditis triage for immunotherapy and intensive monitoring](https://github.com/kayoderaheem/research-portfolio/issues/32) | **1435** | 20 | 7W / 0D / 13L |
| 53 | [#58 — [Idea] Reproducible IFN-response trajectories that separate immune execution from adaptive escape](https://github.com/kayoderaheem/research-portfolio/issues/58) | **1431** | 6 | 0W / 0D / 6L |
| 54 | [#19 — [Idea] Spatially gated ZNF423-stress transitions predicting therapy escape in NF1-associated MPNST](https://github.com/kayoderaheem/research-portfolio/issues/19) | **1427** | 18 | 6W / 0D / 12L |
| 55 | [#29 — [Idea] Defining a clinical-use pathway for urine microRNA as an incremental toxicity biomarker in prostate SBRT](https://github.com/kayoderaheem/research-portfolio/issues/29) | **1424** | 19 | 6W / 0D / 13L |
| 56 | [#6 — [Idea] Mechanical-niche states that forecast glioblastoma radioresistance](https://github.com/kayoderaheem/research-portfolio/issues/6) | **1411** | 18 | 5W / 0D / 13L |
| 57 | [#22 — [Idea] Transportable validation of a therapy-responsive pathogenic immune state in multiple sclerosis](https://github.com/kayoderaheem/research-portfolio/issues/22) | **1401** | 18 | 5W / 0D / 13L |
| 58 | [#21 — [Idea] Decision-value thresholds for multimodal treatment matching in opioid use disorder](https://github.com/kayoderaheem/research-portfolio/issues/21) | **1371** | 16 | 2W / 0D / 14L |
| 59 | [#12 — [Idea] Antigen-presentation escape neighborhoods predicting checkpoint response in melanoma with HIV](https://github.com/kayoderaheem/research-portfolio/issues/12) | **1367** | 16 | 2W / 0D / 14L |

_Last synchronized: 2026-10-07 06:08 UTC._
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

The automation itself runs in GitHub Actions and installs the official GitHub Copilot CLI during a run. The repository owner must have Copilot access that permits Copilot requests from Actions. No long-lived personal access token is stored. OpenAlex and Semantic Scholar work without repository secrets at lower public rate limits; optional `OPENALEX_API_KEY` and `SEMANTIC_SCHOLAR_API_KEY` repository secrets can improve reliability.

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
