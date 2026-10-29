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
| 3 | [#70 — [Idea] Site-transportable decision value of CTA phenotype beyond clinical risk for prolonged EVAR hospitalization](https://github.com/kayoderaheem/research-portfolio/issues/70) | **1629** | 13 | 12W / 0D / 1L |
| 4 | [#80 — [Idea] External validation of a multimodal cerebral venous thrombosis rule-out pathway](https://github.com/kayoderaheem/research-portfolio/issues/80) | **1615** | 12 | 11W / 0D / 1L |
| 5 | [#69 — [Idea] Decision-value thresholds for RNA-proteomic HER2 treatment selection across tumor types](https://github.com/kayoderaheem/research-portfolio/issues/69) | **1613** | 16 | 13W / 0D / 3L |
| 6 | [#28 — [Idea] Incremental decision value and cross-registry calibration of blood-based T2 biomarkers for asthma exacerbation risk](https://github.com/kayoderaheem/research-portfolio/issues/28) | **1611** | 20 | 15W / 0D / 5L |
| 7 | [#24 — [Idea] External calibration of multimodal HCC surveillance triage](https://github.com/kayoderaheem/research-portfolio/issues/24) | **1606** | 22 | 15W / 1D / 6L |
| 8 | [#86 — [Idea] Age-calibrated incremental value of testosterone and creatinine beyond PSA for prostate biopsy triage](https://github.com/kayoderaheem/research-portfolio/issues/86) | **1600** | 16 | 12W / 1D / 3L |
| 9 | [#48 — [Idea] Cross-assay reproducibility of functional drug-sensitivity rankings from clinical tumor samples](https://github.com/kayoderaheem/research-portfolio/issues/48) | **1593** | 12 | 10W / 0D / 2L |
| 10 | [#36 — [Idea] Reference-invariant identification of direct perturbation effects in single-cell models](https://github.com/kayoderaheem/research-portfolio/issues/36) | **1589** | 14 | 11W / 0D / 3L |
| 11 | [#25 — [Idea] Treatment-specific multimodal validation of lupus nephritis response programs](https://github.com/kayoderaheem/research-portfolio/issues/25) | **1586** | 24 | 15W / 1D / 8L |
| 12 | [#56 — [Idea] Exposure-normalized mechanisms of HER2 antibody-drug-conjugate sensitivity and resistance](https://github.com/kayoderaheem/research-portfolio/issues/56) | **1584** | 13 | 10W / 0D / 3L |
| 13 | [#42 — [Idea] Longitudinal MRD-state signatures that distinguish response from refractory escape in multiple myeloma](https://github.com/kayoderaheem/research-portfolio/issues/42) | **1582** | 17 | 12W / 0D / 5L |
| 14 | [#81 — [Idea] Incremental methylation decision value beyond IPSS-M for myelodysplastic neoplasm progression](https://github.com/kayoderaheem/research-portfolio/issues/81) | **1569** | 14 | 10W / 0D / 4L |
| 15 | [#75 — [Idea] External clinical-use validation of MRI-proteomic response prediction in rectal cancer](https://github.com/kayoderaheem/research-portfolio/issues/75) | **1568** | 12 | 9W / 0D / 3L |
| 16 | [#51 — [Idea] Transportable kinase-activity states for predicting drug response across tumor cohorts](https://github.com/kayoderaheem/research-portfolio/issues/51) | **1567** | 14 | 10W / 0D / 4L |
| 17 | [#43 — [Idea] Transportability limits of multimodal drug-response prediction under unseen-drug and unseen-tumor shifts](https://github.com/kayoderaheem/research-portfolio/issues/43) | **1565** | 24 | 15W / 0D / 9L |
| 18 | [#31 — [Idea] Site-transportable multimodal validation of corneal nerve imaging for small-fiber neuropathy](https://github.com/kayoderaheem/research-portfolio/issues/31) | **1560** | 30 | 18W / 0D / 12L |
| 19 | [#73 — [Idea] Incremental decision value of hormonal and lifestyle signals for PCOS diagnostic triage](https://github.com/kayoderaheem/research-portfolio/issues/73) | **1559** | 15 | 10W / 0D / 5L |
| 20 | [#78 — [Idea] Incremental decision value of ultrasound-enhanced airway risk stratification across clinical populations](https://github.com/kayoderaheem/research-portfolio/issues/78) | **1558** | 15 | 10W / 0D / 5L |
| 21 | [#90 — [Idea] Prospective limits of virtual-cell extrapolation across regenerative history](https://github.com/kayoderaheem/research-portfolio/issues/90) | **1557** | 14 | 9W / 1D / 4L |
| 22 | [#63 — [Idea] UCHL1-defined dendritic-cell–Treg neighborhoods as a resistance mechanism to Atezo/Bev in hepatocellular carcinoma](https://github.com/kayoderaheem/research-portfolio/issues/63) | **1557** | 17 | 11W / 0D / 6L |
| 23 | [#61 — [Idea] Spatially resolved IGF2BP3–MHC-I competence as an incremental checkpoint-response predictor in triple-negative breast cancer](https://github.com/kayoderaheem/research-portfolio/issues/61) | **1555** | 15 | 10W / 0D / 5L |
| 24 | [#71 — [Idea] Dynamic clinical-imaging-molecular calibration for treatment-aware risk in anti-MDA5 dermatomyositis-associated ILD](https://github.com/kayoderaheem/research-portfolio/issues/71) | **1553** | 13 | 9W / 0D / 4L |
| 25 | [#17 — [Idea] Patient-level tissue-context gain over composition for multimodal lymphoma treatment-response prediction](https://github.com/kayoderaheem/research-portfolio/issues/17) | **1550** | 25 | 15W / 0D / 10L |
| 26 | [#84 — [Idea] Decision value of vital-sign and medication signals beyond BIS for early deep-anesthesia warnings](https://github.com/kayoderaheem/research-portfolio/issues/84) | **1543** | 16 | 10W / 0D / 6L |
| 27 | [#83 — [Idea] Decision value of lymphocyte trajectories for early anti-drug-antibody testing during natalizumab therapy](https://github.com/kayoderaheem/research-portfolio/issues/83) | **1543** | 14 | 9W / 0D / 5L |
| 28 | [#27 — [Idea] Decision-value and site-transportable calibration of temporal multimodal deterioration risk in ICU care](https://github.com/kayoderaheem/research-portfolio/issues/27) | **1542** | 33 | 18W / 0D / 15L |
| 29 | [#45 — [Idea] Incremental treatment-decision value of functional drug screening beyond genomic matching in pediatric brain tumors](https://github.com/kayoderaheem/research-portfolio/issues/45) | **1542** | 19 | 11W / 0D / 8L |
| 30 | [#87 — [Idea] Spatially identifiable virtual-cell responses to unseen intracellular perturbations](https://github.com/kayoderaheem/research-portfolio/issues/87) | **1533** | 17 | 10W / 0D / 7L |
| 31 | [#60 — [Idea] Spatial cGAS–STING–fibrosis boundaries that determine combined TACE–checkpoint response](https://github.com/kayoderaheem/research-portfolio/issues/60) | **1523** | 16 | 9W / 0D / 7L |
| 32 | [#2 — [Idea] Transportable response signatures for molecularly matched therapy in advanced pancreatic cancer](https://github.com/kayoderaheem/research-portfolio/issues/2) | **1521** | 32 | 17W / 0D / 15L |
| 33 | [#39 — [Idea] Composition-aware counterfactuals for unseen perturbations across tissue neighborhoods](https://github.com/kayoderaheem/research-portfolio/issues/39) | **1521** | 26 | 14W / 0D / 12L |
| 34 | [#1 — [Idea] Time-to-decision functional profiling for resistance-aware combination therapy](https://github.com/kayoderaheem/research-portfolio/issues/1) | **1521** | 39 | 20W / 0D / 19L |
| 35 | [#13 — [Idea] Spatial CAF–immune buffering of EGFR-targeted therapy in lung adenocarcinoma](https://github.com/kayoderaheem/research-portfolio/issues/13) | **1520** | 37 | 19W / 0D / 18L |
| 36 | [#65 — [Idea] Spatial fibroblast-state transitions as predictors of bazedoxifene response in cutaneous fibrosis](https://github.com/kayoderaheem/research-portfolio/issues/65) | **1520** | 18 | 10W / 0D / 8L |
| 37 | [#15 — [Idea] BMP-restraint failure and BCL2-high niches as predictors of diffuse gastric cancer treatment response](https://github.com/kayoderaheem/research-portfolio/issues/15) | **1516** | 36 | 18W / 1D / 17L |
| 38 | [#40 — [Idea] Context-aware virtual screening of apoptosis combinations in germ cell tumors](https://github.com/kayoderaheem/research-portfolio/issues/40) | **1513** | 30 | 15W / 1D / 14L |
| 39 | [#55 — [Idea] Mutation-specific target engagement as a separator of intrinsic sensitivity and resistance](https://github.com/kayoderaheem/research-portfolio/issues/55) | **1511** | 15 | 8W / 0D / 7L |
| 40 | [#93 — [Idea] Mechanism-identifiable virtual cells for bioenergetic perturbations](https://github.com/kayoderaheem/research-portfolio/issues/93) | **1511** | 13 | 7W / 0D / 6L |
| 41 | [#92 — [Idea] Assay-transportable virtual-cell predictions from fresh to fixed tissue](https://github.com/kayoderaheem/research-portfolio/issues/92) | **1507** | 13 | 7W / 0D / 6L |
| 42 | [#85 — [Idea] Particle-fraction-specific blood RNA value for clinically defined Alzheimer’s disease triage](https://github.com/kayoderaheem/research-portfolio/issues/85) | **1505** | 17 | 9W / 0D / 8L |
| 43 | [#57 — [Idea] Pre-existing stromal architecture as an incremental predictor of bispecific-antibody response](https://github.com/kayoderaheem/research-portfolio/issues/57) | **1504** | 22 | 11W / 0D / 11L |
| 44 | [#76 — [Idea] Population- and site-calibrated multimodal fibrosis triage in pediatric MASLD](https://github.com/kayoderaheem/research-portfolio/issues/76) | **1503** | 16 | 8W / 0D / 8L |
| 45 | [#98 — [Idea] Virtual-cell identifiability of cooperative histone-code perturbations](https://github.com/kayoderaheem/research-portfolio/issues/98) | **1491** | 15 | 7W / 0D / 8L |
| 46 | [#91 — [Idea] Kinetic identifiability of acute transcriptional perturbations in virtual cells](https://github.com/kayoderaheem/research-portfolio/issues/91) | **1491** | 17 | 8W / 0D / 9L |
| 47 | [#66 — [Idea] Architecture-aware prediction of treatment response in glioblastoma beyond cellular composition](https://github.com/kayoderaheem/research-portfolio/issues/66) | **1487** | 15 | 7W / 0D / 8L |
| 48 | [#89 — [Idea] Context-transfer limits of virtual cells for stress-history perturbations](https://github.com/kayoderaheem/research-portfolio/issues/89) | **1487** | 13 | 6W / 0D / 7L |
| 49 | [#67 — [Idea] Schwann-cell niche gating of reproducible chemotherapy-escape transitions in neuroblastoma](https://github.com/kayoderaheem/research-portfolio/issues/67) | **1485** | 19 | 9W / 0D / 10L |
| 50 | [#37 — [Idea] Prospective falsification of multimodal virtual-cell predictions for regulatory-state perturbations](https://github.com/kayoderaheem/research-portfolio/issues/37) | **1481** | 34 | 16W / 0D / 18L |
| 51 | [#7 — [Idea] Reproducible adaptive cell-state transitions after KRAS pathway blockade](https://github.com/kayoderaheem/research-portfolio/issues/7) | **1479** | 42 | 20W / 0D / 22L |
| 52 | [#9 — [Idea] Spatially resolved IL-17 and retinoid states predicting tunnel-directed therapy response in hidradenitis suppurativa](https://github.com/kayoderaheem/research-portfolio/issues/9) | **1478** | 31 | 14W / 1D / 16L |
| 53 | [#62 — [Idea] Reproducible tumor–lung interface ERK adaptation after MCL1 inhibition](https://github.com/kayoderaheem/research-portfolio/issues/62) | **1478** | 26 | 12W / 0D / 14L |
| 54 | [#96 — [Idea] Counterfactual virtual cells for FGF-driven oligodendrocyte state transitions](https://github.com/kayoderaheem/research-portfolio/issues/96) | **1476** | 16 | 7W / 0D / 9L |
| 55 | [#41 — [Idea] Falsifying resettable virtual-cell models of quiescent chromatin](https://github.com/kayoderaheem/research-portfolio/issues/41) | **1468** | 29 | 13W / 0D / 16L |
| 56 | [#77 — [Idea] Multimodal discrimination of active disease from persistent MRI lesions in intracranial tuberculoma](https://github.com/kayoderaheem/research-portfolio/issues/77) | **1468** | 15 | 6W / 0D / 9L |
| 57 | [#23 — [Idea] Incremental value of dynamic inflammation for recovery-guided rehabilitation after knee arthroplasty](https://github.com/kayoderaheem/research-portfolio/issues/23) | **1468** | 31 | 14W / 0D / 17L |
| 58 | [#10 — [Idea] Metabolite-defined resident-memory niches that determine checkpoint response in hepatocellular carcinoma](https://github.com/kayoderaheem/research-portfolio/issues/10) | **1468** | 33 | 15W / 0D / 18L |
| 59 | [#97 — [Idea] Virtual-cell prediction of mechanical recovery and alveolar niche memory](https://github.com/kayoderaheem/research-portfolio/issues/97) | **1467** | 13 | 5W / 0D / 8L |
| 60 | [#88 — [Idea] Prospective falsification of chromatin-to-expression counterfactuals](https://github.com/kayoderaheem/research-portfolio/issues/88) | **1467** | 13 | 5W / 0D / 8L |
| 61 | [#59 — [Idea] Spatial access states that determine engineered T-cell treatment response](https://github.com/kayoderaheem/research-portfolio/issues/59) | **1466** | 13 | 5W / 0D / 8L |
| 62 | [#53 — [Idea] Early treatment-decision value of heterogeneity trajectories in HER2-targeted bladder cancer](https://github.com/kayoderaheem/research-portfolio/issues/53) | **1466** | 19 | 8W / 0D / 11L |
| 63 | [#18 — [Idea] Spatially resolved metabolic-inflammatory routes to gemcitabine resistance in cholangiocarcinoma](https://github.com/kayoderaheem/research-portfolio/issues/18) | **1465** | 30 | 13W / 1D / 16L |
| 64 | [#49 — [Idea] Exposure-adjusted phosphoproteomic signatures of pharmacologic failure versus biological resistance](https://github.com/kayoderaheem/research-portfolio/issues/49) | **1465** | 17 | 7W / 0D / 10L |
| 65 | [#8 — [Idea] Metastatic-site spatial niches that modify ALK-inhibitor response](https://github.com/kayoderaheem/research-portfolio/issues/8) | **1464** | 25 | 11W / 0D / 14L |
| 66 | [#52 — [Idea] Isoform-switching mechanisms that separate intrinsic from acquired drug resistance](https://github.com/kayoderaheem/research-portfolio/issues/52) | **1464** | 15 | 6W / 0D / 9L |
| 67 | [#68 — [Idea] Local IL-15 access states as predictors of innate-cell therapy response in brain metastases](https://github.com/kayoderaheem/research-portfolio/issues/68) | **1464** | 17 | 7W / 0D / 10L |
| 68 | [#50 — [Idea] Population-calibrated pharmacogenomic prediction of tamoxifen benefit and endocrine resistance](https://github.com/kayoderaheem/research-portfolio/issues/50) | **1464** | 19 | 8W / 0D / 11L |
| 69 | [#54 — [Idea] Persistence and specificity of treatment-induced T-cell clones as a response discriminator in checkpoint therapy](https://github.com/kayoderaheem/research-portfolio/issues/54) | **1463** | 17 | 7W / 0D / 10L |
| 70 | [#11 — [Idea] Spatially constrained T-cell fitness states predicting blinatumomab response in B-cell leukemia](https://github.com/kayoderaheem/research-portfolio/issues/11) | **1461** | 29 | 12W / 1D / 16L |
| 71 | [#5 — [Idea] Spatially resolved immune-priming trajectories during cervical chemoradiotherapy](https://github.com/kayoderaheem/research-portfolio/issues/5) | **1460** | 22 | 8W / 3D / 11L |
| 72 | [#38 — [Idea] Cross-species identifiability of conserved versus context-specific perturbation responses](https://github.com/kayoderaheem/research-portfolio/issues/38) | **1459** | 16 | 6W / 0D / 10L |
| 73 | [#35 — [Idea] Causal transfer of chromatin-to-expression perturbation models across ATRX-deficient sarcoma states](https://github.com/kayoderaheem/research-portfolio/issues/35) | **1458** | 18 | 7W / 0D / 11L |
| 74 | [#32 — [Idea] Clinical-use validation of multimodal myocarditis triage for immunotherapy and intensive monitoring](https://github.com/kayoderaheem/research-portfolio/issues/32) | **1458** | 24 | 10W / 0D / 14L |
| 75 | [#64 — [Idea] Myeloid-primed necrosis trajectories predict STING-agonist response in osteosarcoma](https://github.com/kayoderaheem/research-portfolio/issues/64) | **1453** | 16 | 6W / 0D / 10L |
| 76 | [#82 — [Idea] Clinical-use validation of multimodal GFAP trajectory monitoring in pediatric Alexander disease](https://github.com/kayoderaheem/research-portfolio/issues/82) | **1453** | 12 | 4W / 0D / 8L |
| 77 | [#3 — [Idea] Early detection of DNA-damage-tolerance escape during genotoxic therapy](https://github.com/kayoderaheem/research-portfolio/issues/3) | **1451** | 26 | 11W / 0D / 15L |
| 78 | [#19 — [Idea] Spatially gated ZNF423-stress transitions predicting therapy escape in NF1-associated MPNST](https://github.com/kayoderaheem/research-portfolio/issues/19) | **1450** | 22 | 9W / 0D / 13L |
| 79 | [#4 — [Idea] Reproducible myeloid-niche remodeling as a determinant of metastatic immunotherapy response](https://github.com/kayoderaheem/research-portfolio/issues/4) | **1450** | 27 | 11W / 1D / 15L |
| 80 | [#34 — [Idea] Prospective falsification of a dynamic proteomic virtual cell across unseen therapies and organoid contexts](https://github.com/kayoderaheem/research-portfolio/issues/34) | **1450** | 18 | 7W / 0D / 11L |
| 81 | [#26 — [Idea] Site-robust multimodal risk stratification for fetal growth restriction management](https://github.com/kayoderaheem/research-portfolio/issues/26) | **1450** | 24 | 10W / 0D / 14L |
| 82 | [#46 — [Idea] TET2-mutant clonal-hematopoiesis macrophages as a reversible cause of BRAF/MEK resistance in anaplastic thyroid cancer](https://github.com/kayoderaheem/research-portfolio/issues/46) | **1447** | 12 | 3W / 1D / 8L |
| 83 | [#29 — [Idea] Defining a clinical-use pathway for urine microRNA as an incremental toxicity biomarker in prostate SBRT](https://github.com/kayoderaheem/research-portfolio/issues/29) | **1434** | 22 | 8W / 0D / 14L |
| 84 | [#79 — [Idea] Pathogen-aware multimodal calibration for pulmonary sepsis treatment selection](https://github.com/kayoderaheem/research-portfolio/issues/79) | **1431** | 12 | 3W / 0D / 9L |
| 85 | [#44 — [Idea] Early functional detection of hypoxia-mediated resistance before radiographic treatment failure](https://github.com/kayoderaheem/research-portfolio/issues/44) | **1431** | 22 | 8W / 0D / 14L |
| 86 | [#74 — [Idea] Site-calibrated maternal-placental-fetal multimodal risk stratification for neonatal immune-metabolic follow-up](https://github.com/kayoderaheem/research-portfolio/issues/74) | **1431** | 12 | 3W / 0D / 9L |
| 87 | [#94 — [Idea] Paracrine-aware virtual cells for engineered astrocyte perturbations](https://github.com/kayoderaheem/research-portfolio/issues/94) | **1431** | 14 | 4W / 0D / 10L |
| 88 | [#22 — [Idea] Transportable validation of a therapy-responsive pathogenic immune state in multiple sclerosis](https://github.com/kayoderaheem/research-portfolio/issues/22) | **1413** | 19 | 6W / 0D / 13L |
| 89 | [#58 — [Idea] Reproducible IFN-response trajectories that separate immune execution from adaptive escape](https://github.com/kayoderaheem/research-portfolio/issues/58) | **1407** | 16 | 4W / 0D / 12L |
| 90 | [#72 — [Idea] Clinical-use validation of YTHDC1 condensate state as a treatment-selection biomarker for METTL3 inhibition](https://github.com/kayoderaheem/research-portfolio/issues/72) | **1400** | 17 | 4W / 0D / 13L |
| 91 | [#47 — [Idea] Cross-cancer validation of lactate-transport states as predictors of drug-tolerant persistence](https://github.com/kayoderaheem/research-portfolio/issues/47) | **1395** | 15 | 3W / 0D / 12L |
| 92 | [#6 — [Idea] Mechanical-niche states that forecast glioblastoma radioresistance](https://github.com/kayoderaheem/research-portfolio/issues/6) | **1386** | 20 | 5W / 0D / 15L |
| 93 | [#21 — [Idea] Decision-value thresholds for multimodal treatment matching in opioid use disorder](https://github.com/kayoderaheem/research-portfolio/issues/21) | **1385** | 17 | 3W / 0D / 14L |
| 94 | [#12 — [Idea] Antigen-presentation escape neighborhoods predicting checkpoint response in melanoma with HIV](https://github.com/kayoderaheem/research-portfolio/issues/12) | **1367** | 16 | 2W / 0D / 14L |
| 95 | [#95 — [Idea] Evolution-aware virtual cells for unseen therapy resistance states](https://github.com/kayoderaheem/research-portfolio/issues/95) | **1365** | 12 | 0W / 0D / 12L |

_Last synchronized: 2026-10-29 18:31 UTC._
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
