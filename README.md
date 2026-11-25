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
| 4 | [#100 — [Idea] Decision-preserving transport of ex vivo endocrine sensitivity across institutions](https://github.com/kayoderaheem/research-portfolio/issues/100) | **1624** | 11 | 11W / 0D / 0L |
| 5 | [#80 — [Idea] External validation of a multimodal cerebral venous thrombosis rule-out pathway](https://github.com/kayoderaheem/research-portfolio/issues/80) | **1615** | 12 | 11W / 0D / 1L |
| 6 | [#69 — [Idea] Decision-value thresholds for RNA-proteomic HER2 treatment selection across tumor types](https://github.com/kayoderaheem/research-portfolio/issues/69) | **1613** | 16 | 13W / 0D / 3L |
| 7 | [#28 — [Idea] Incremental decision value and cross-registry calibration of blood-based T2 biomarkers for asthma exacerbation risk](https://github.com/kayoderaheem/research-portfolio/issues/28) | **1611** | 20 | 15W / 0D / 5L |
| 8 | [#24 — [Idea] External calibration of multimodal HCC surveillance triage](https://github.com/kayoderaheem/research-portfolio/issues/24) | **1606** | 22 | 15W / 1D / 6L |
| 9 | [#126 — [Idea] Clinical decision value and site calibration of multimodal AI-ECG for occlusion myocardial infarction triage](https://github.com/kayoderaheem/research-portfolio/issues/126) | **1600** | 11 | 10W / 0D / 1L |
| 10 | [#86 — [Idea] Age-calibrated incremental value of testosterone and creatinine beyond PSA for prostate biopsy triage](https://github.com/kayoderaheem/research-portfolio/issues/86) | **1600** | 16 | 12W / 1D / 3L |
| 11 | [#48 — [Idea] Cross-assay reproducibility of functional drug-sensitivity rankings from clinical tumor samples](https://github.com/kayoderaheem/research-portfolio/issues/48) | **1593** | 12 | 10W / 0D / 2L |
| 12 | [#144 — [Idea] Representation coverage gates unseen genetic perturbation prediction](https://github.com/kayoderaheem/research-portfolio/issues/144) | **1592** | 10 | 9W / 0D / 1L |
| 13 | [#120 — [Idea] State-conditioned coherence as a transportable measure of single-cell treatment response](https://github.com/kayoderaheem/research-portfolio/issues/120) | **1592** | 10 | 9W / 0D / 1L |
| 14 | [#129 — [Idea] Calibrated functional–clinical classification of KCNH2 variants for long-QT management](https://github.com/kayoderaheem/research-portfolio/issues/129) | **1592** | 10 | 9W / 0D / 1L |
| 15 | [#135 — [Idea] External validation of morphology-laboratory risk stratification after ruptured hepatocellular carcinoma](https://github.com/kayoderaheem/research-portfolio/issues/135) | **1590** | 10 | 9W / 0D / 1L |
| 16 | [#102 — [Idea] External validation of ratiometric combination-response signals in pediatric leukemia](https://github.com/kayoderaheem/research-portfolio/issues/102) | **1590** | 10 | 9W / 0D / 1L |
| 17 | [#36 — [Idea] Reference-invariant identification of direct perturbation effects in single-cell models](https://github.com/kayoderaheem/research-portfolio/issues/36) | **1589** | 14 | 11W / 0D / 3L |
| 18 | [#25 — [Idea] Treatment-specific multimodal validation of lupus nephritis response programs](https://github.com/kayoderaheem/research-portfolio/issues/25) | **1586** | 24 | 15W / 1D / 8L |
| 19 | [#56 — [Idea] Exposure-normalized mechanisms of HER2 antibody-drug-conjugate sensitivity and resistance](https://github.com/kayoderaheem/research-portfolio/issues/56) | **1584** | 13 | 10W / 0D / 3L |
| 20 | [#42 — [Idea] Longitudinal MRD-state signatures that distinguish response from refractory escape in multiple myeloma](https://github.com/kayoderaheem/research-portfolio/issues/42) | **1582** | 17 | 12W / 0D / 5L |
| 21 | [#123 — [Idea] Decision-value decomposition of radiomics and EBV DNA for adaptive nasopharyngeal radiotherapy](https://github.com/kayoderaheem/research-portfolio/issues/123) | **1580** | 11 | 9W / 0D / 2L |
| 22 | [#43 — [Idea] Transportability limits of multimodal drug-response prediction under unseen-drug and unseen-tumor shifts](https://github.com/kayoderaheem/research-portfolio/issues/43) | **1577** | 25 | 16W / 0D / 9L |
| 23 | [#17 — [Idea] Patient-level tissue-context gain over composition for multimodal lymphoma treatment-response prediction](https://github.com/kayoderaheem/research-portfolio/issues/17) | **1574** | 27 | 17W / 0D / 10L |
| 24 | [#63 — [Idea] UCHL1-defined dendritic-cell–Treg neighborhoods as a resistance mechanism to Atezo/Bev in hepatocellular carcinoma](https://github.com/kayoderaheem/research-portfolio/issues/63) | **1571** | 20 | 13W / 0D / 7L |
| 25 | [#75 — [Idea] External clinical-use validation of MRI-proteomic response prediction in rectal cancer](https://github.com/kayoderaheem/research-portfolio/issues/75) | **1569** | 14 | 10W / 0D / 4L |
| 26 | [#81 — [Idea] Incremental methylation decision value beyond IPSS-M for myelodysplastic neoplasm progression](https://github.com/kayoderaheem/research-portfolio/issues/81) | **1569** | 14 | 10W / 0D / 4L |
| 27 | [#147 — [Idea] Reliability-gated extrapolation for combinatorial perturbations](https://github.com/kayoderaheem/research-portfolio/issues/147) | **1565** | 10 | 8W / 0D / 2L |
| 28 | [#121 — [Idea] Spatially anchored endocrine-response states in ER-positive breast cancer](https://github.com/kayoderaheem/research-portfolio/issues/121) | **1558** | 11 | 8W / 0D / 3L |
| 29 | [#61 — [Idea] Spatially resolved IGF2BP3–MHC-I competence as an incremental checkpoint-response predictor in triple-negative breast cancer](https://github.com/kayoderaheem/research-portfolio/issues/61) | **1558** | 19 | 12W / 0D / 7L |
| 30 | [#136 — [Idea] Incremental decision value of retinal imaging beyond clinical cardiovascular risk assessment](https://github.com/kayoderaheem/research-portfolio/issues/136) | **1544** | 10 | 7W / 0D / 3L |
| 31 | [#78 — [Idea] Incremental decision value of ultrasound-enhanced airway risk stratification across clinical populations](https://github.com/kayoderaheem/research-portfolio/issues/78) | **1544** | 20 | 12W / 0D / 8L |
| 32 | [#108 — [Idea] Causal testing of CD44v9 persistence as a reversible driver of pancreatic cancer drug resistance](https://github.com/kayoderaheem/research-portfolio/issues/108) | **1544** | 10 | 7W / 0D / 3L |
| 33 | [#131 — [Idea] External clinical-use validation of multimodal tarsal tunnel diagnosis](https://github.com/kayoderaheem/research-portfolio/issues/131) | **1544** | 8 | 6W / 0D / 2L |
| 34 | [#39 — [Idea] Composition-aware counterfactuals for unseen perturbations across tissue neighborhoods](https://github.com/kayoderaheem/research-portfolio/issues/39) | **1543** | 30 | 17W / 0D / 13L |
| 35 | [#132 — [Idea] Incremental multimodal arrhythmic-risk value for genotype-informed ICD decisions in dilated cardiomyopathy](https://github.com/kayoderaheem/research-portfolio/issues/132) | **1543** | 12 | 8W / 0D / 4L |
| 36 | [#84 — [Idea] Decision value of vital-sign and medication signals beyond BIS for early deep-anesthesia warnings](https://github.com/kayoderaheem/research-portfolio/issues/84) | **1542** | 18 | 11W / 0D / 7L |
| 37 | [#27 — [Idea] Decision-value and site-transportable calibration of temporal multimodal deterioration risk in ICU care](https://github.com/kayoderaheem/research-portfolio/issues/27) | **1542** | 33 | 18W / 0D / 15L |
| 38 | [#45 — [Idea] Incremental treatment-decision value of functional drug screening beyond genomic matching in pediatric brain tumors](https://github.com/kayoderaheem/research-portfolio/issues/45) | **1542** | 19 | 11W / 0D / 8L |
| 39 | [#83 — [Idea] Decision value of lymphocyte trajectories for early anti-drug-antibody testing during natalizumab therapy](https://github.com/kayoderaheem/research-portfolio/issues/83) | **1542** | 16 | 10W / 0D / 6L |
| 40 | [#71 — [Idea] Dynamic clinical-imaging-molecular calibration for treatment-aware risk in anti-MDA5 dermatomyositis-associated ILD](https://github.com/kayoderaheem/research-portfolio/issues/71) | **1542** | 14 | 9W / 0D / 5L |
| 41 | [#138 — [Idea] Abstention-calibrated virtual cells for unseen combinations and doses](https://github.com/kayoderaheem/research-portfolio/issues/138) | **1541** | 12 | 8W / 0D / 4L |
| 42 | [#31 — [Idea] Site-transportable multimodal validation of corneal nerve imaging for small-fiber neuropathy](https://github.com/kayoderaheem/research-portfolio/issues/31) | **1537** | 34 | 19W / 0D / 15L |
| 43 | [#141 — [Idea] Counterfactual identifiability of airway interferon cell-type effects](https://github.com/kayoderaheem/research-portfolio/issues/141) | **1536** | 12 | 7W / 1D / 4L |
| 44 | [#148 — [Idea] Falsifiable context transfer for NGLY1 microglial perturbations](https://github.com/kayoderaheem/research-portfolio/issues/148) | **1536** | 7 | 5W / 0D / 2L |
| 45 | [#112 — [Idea] Incremental predictive value of spatial immune fronts during electrochemotherapy](https://github.com/kayoderaheem/research-portfolio/issues/112) | **1536** | 11 | 7W / 0D / 4L |
| 46 | [#106 — [Idea] Replicate-aware prediction of actionable resistance trajectories under targeted therapy](https://github.com/kayoderaheem/research-portfolio/issues/106) | **1535** | 7 | 5W / 0D / 2L |
| 47 | [#60 — [Idea] Spatial cGAS–STING–fibrosis boundaries that determine combined TACE–checkpoint response](https://github.com/kayoderaheem/research-portfolio/issues/60) | **1535** | 17 | 10W / 0D / 7L |
| 48 | [#73 — [Idea] Incremental decision value of hormonal and lifestyle signals for PCOS diagnostic triage](https://github.com/kayoderaheem/research-portfolio/issues/73) | **1535** | 17 | 10W / 0D / 7L |
| 49 | [#87 — [Idea] Spatially identifiable virtual-cell responses to unseen intracellular perturbations](https://github.com/kayoderaheem/research-portfolio/issues/87) | **1535** | 19 | 11W / 0D / 8L |
| 50 | [#118 — [Idea] Endothelial maturation niches as a tissue-context predictor of breast cancer treatment response](https://github.com/kayoderaheem/research-portfolio/issues/118) | **1535** | 9 | 6W / 0D / 3L |
| 51 | [#145 — [Idea] Falsifying hypoxia-aware ARG2 counterfactuals in engineered T cells](https://github.com/kayoderaheem/research-portfolio/issues/145) | **1535** | 7 | 5W / 0D / 2L |
| 52 | [#90 — [Idea] Prospective limits of virtual-cell extrapolation across regenerative history](https://github.com/kayoderaheem/research-portfolio/issues/90) | **1534** | 16 | 9W / 1D / 6L |
| 53 | [#104 — [Idea] Sex-stratified transportability of immune-response signals under checkpoint therapy](https://github.com/kayoderaheem/research-portfolio/issues/104) | **1534** | 9 | 6W / 0D / 3L |
| 54 | [#139 — [Idea] Genotype-by-environment limits of virtual-cell extrapolation during state transitions](https://github.com/kayoderaheem/research-portfolio/issues/139) | **1534** | 9 | 6W / 0D / 3L |
| 55 | [#51 — [Idea] Transportable kinase-activity states for predicting drug response across tumor cohorts](https://github.com/kayoderaheem/research-portfolio/issues/51) | **1534** | 17 | 10W / 0D / 7L |
| 56 | [#2 — [Idea] Transportable response signatures for molecularly matched therapy in advanced pancreatic cancer](https://github.com/kayoderaheem/research-portfolio/issues/2) | **1533** | 35 | 19W / 0D / 16L |
| 57 | [#149 — [Idea] Prospective falsification of melanoma IFN-gamma virtual-cell dynamics](https://github.com/kayoderaheem/research-portfolio/issues/149) | **1523** | 12 | 7W / 0D / 5L |
| 58 | [#140 — [Idea] Identifying cytosolic-access effects in perturbation-response models](https://github.com/kayoderaheem/research-portfolio/issues/140) | **1522** | 12 | 7W / 0D / 5L |
| 59 | [#134 — [Idea] External decision validation of gut-brain multimodal biomarkers for post-stroke cognitive impairment](https://github.com/kayoderaheem/research-portfolio/issues/134) | **1521** | 8 | 5W / 0D / 3L |
| 60 | [#127 — [Idea] Incremental decision value of atlas-anchored urine compartments for early diabetic kidney disease staging](https://github.com/kayoderaheem/research-portfolio/issues/127) | **1519** | 12 | 7W / 0D / 5L |
| 61 | [#114 — [Idea] DOK3-CARD9 macrophage-state transitions as reproducible determinants of PD-1 blockade response](https://github.com/kayoderaheem/research-portfolio/issues/114) | **1512** | 21 | 11W / 0D / 10L |
| 62 | [#91 — [Idea] Kinetic identifiability of acute transcriptional perturbations in virtual cells](https://github.com/kayoderaheem/research-portfolio/issues/91) | **1506** | 23 | 11W / 1D / 11L |
| 63 | [#85 — [Idea] Particle-fraction-specific blood RNA value for clinically defined Alzheimer’s disease triage](https://github.com/kayoderaheem/research-portfolio/issues/85) | **1504** | 21 | 11W / 0D / 10L |
| 64 | [#93 — [Idea] Mechanism-identifiable virtual cells for bioenergetic perturbations](https://github.com/kayoderaheem/research-portfolio/issues/93) | **1494** | 29 | 14W / 0D / 15L |
| 65 | [#98 — [Idea] Virtual-cell identifiability of cooperative histone-code perturbations](https://github.com/kayoderaheem/research-portfolio/issues/98) | **1480** | 18 | 8W / 0D / 10L |
| 66 | [#77 — [Idea] Multimodal discrimination of active disease from persistent MRI lesions in intracranial tuberculoma](https://github.com/kayoderaheem/research-portfolio/issues/77) | **1480** | 16 | 7W / 0D / 9L |
| 67 | [#130 — [Idea] Congestion-aware multimodal prediction of cardiovascular drug exposure and response](https://github.com/kayoderaheem/research-portfolio/issues/130) | **1480** | 12 | 5W / 0D / 7L |
| 68 | [#66 — [Idea] Architecture-aware prediction of treatment response in glioblastoma beyond cellular composition](https://github.com/kayoderaheem/research-portfolio/issues/66) | **1477** | 30 | 14W / 0D / 16L |
| 69 | [#133 — [Idea] Decision-value decomposition of photon-counting CT and MRI for molecularly informed colorectal liver metastasis management](https://github.com/kayoderaheem/research-portfolio/issues/133) | **1477** | 10 | 4W / 0D / 6L |
| 70 | [#119 — [Idea] Spatial immune organization as a predictor of oncolytic virotherapy response in glioma](https://github.com/kayoderaheem/research-portfolio/issues/119) | **1477** | 12 | 5W / 0D / 7L |
| 71 | [#55 — [Idea] Mutation-specific target engagement as a separator of intrinsic sensitivity and resistance](https://github.com/kayoderaheem/research-portfolio/issues/55) | **1476** | 28 | 13W / 0D / 15L |
| 72 | [#101 — [Idea] Separating pre-existing from therapy-selected resistance in relapsed lymphoma](https://github.com/kayoderaheem/research-portfolio/issues/101) | **1476** | 18 | 8W / 0D / 10L |
| 73 | [#99 — [Idea] Abstention-calibrated molecular treatment recommendations for precision oncology](https://github.com/kayoderaheem/research-portfolio/issues/99) | **1476** | 16 | 7W / 0D / 9L |
| 74 | [#117 — [Idea] Reproducible treatment-induced state transitions after epigenetic therapy in gastric cancer](https://github.com/kayoderaheem/research-portfolio/issues/117) | **1475** | 16 | 7W / 0D / 9L |
| 75 | [#105 — [Idea] Bone-niche dependence of functional drug response in multiple myeloma](https://github.com/kayoderaheem/research-portfolio/issues/105) | **1475** | 20 | 9W / 0D / 11L |
| 76 | [#13 — [Idea] Spatial CAF–immune buffering of EGFR-targeted therapy in lung adenocarcinoma](https://github.com/kayoderaheem/research-portfolio/issues/13) | **1474** | 41 | 19W / 0D / 22L |
| 77 | [#89 — [Idea] Context-transfer limits of virtual cells for stress-history perturbations](https://github.com/kayoderaheem/research-portfolio/issues/89) | **1474** | 18 | 8W / 0D / 10L |
| 78 | [#1 — [Idea] Time-to-decision functional profiling for resistance-aware combination therapy](https://github.com/kayoderaheem/research-portfolio/issues/1) | **1474** | 45 | 21W / 0D / 24L |
| 79 | [#116 — [Idea] Pre-treatment immune niches that forecast glucocorticoid response in granulomatous lobular mastitis](https://github.com/kayoderaheem/research-portfolio/issues/116) | **1474** | 8 | 3W / 0D / 5L |
| 80 | [#67 — [Idea] Schwann-cell niche gating of reproducible chemotherapy-escape transitions in neuroblastoma](https://github.com/kayoderaheem/research-portfolio/issues/67) | **1473** | 20 | 9W / 0D / 11L |
| 81 | [#57 — [Idea] Pre-existing stromal architecture as an incremental predictor of bispecific-antibody response](https://github.com/kayoderaheem/research-portfolio/issues/57) | **1473** | 35 | 16W / 0D / 19L |
| 82 | [#7 — [Idea] Reproducible adaptive cell-state transitions after KRAS pathway blockade](https://github.com/kayoderaheem/research-portfolio/issues/7) | **1471** | 45 | 21W / 0D / 24L |
| 83 | [#65 — [Idea] Spatial fibroblast-state transitions as predictors of bazedoxifene response in cutaneous fibrosis](https://github.com/kayoderaheem/research-portfolio/issues/65) | **1471** | 29 | 13W / 0D / 16L |
| 84 | [#37 — [Idea] Prospective falsification of multimodal virtual-cell predictions for regulatory-state perturbations](https://github.com/kayoderaheem/research-portfolio/issues/37) | **1471** | 35 | 16W / 0D / 19L |
| 85 | [#15 — [Idea] BMP-restraint failure and BCL2-high niches as predictors of diffuse gastric cancer treatment response](https://github.com/kayoderaheem/research-portfolio/issues/15) | **1470** | 40 | 18W / 1D / 21L |
| 86 | [#92 — [Idea] Assay-transportable virtual-cell predictions from fresh to fixed tissue](https://github.com/kayoderaheem/research-portfolio/issues/92) | **1470** | 18 | 8W / 0D / 10L |
| 87 | [#35 — [Idea] Causal transfer of chromatin-to-expression perturbation models across ATRX-deficient sarcoma states](https://github.com/kayoderaheem/research-portfolio/issues/35) | **1470** | 19 | 8W / 0D / 11L |
| 88 | [#76 — [Idea] Population- and site-calibrated multimodal fibrosis triage in pediatric MASLD](https://github.com/kayoderaheem/research-portfolio/issues/76) | **1470** | 23 | 10W / 0D / 13L |
| 89 | [#137 — [Idea] Decision value of autonomic recovery monitoring after cardiac surgery](https://github.com/kayoderaheem/research-portfolio/issues/137) | **1469** | 9 | 3W / 0D / 6L |
| 90 | [#10 — [Idea] Metabolite-defined resident-memory niches that determine checkpoint response in hepatocellular carcinoma](https://github.com/kayoderaheem/research-portfolio/issues/10) | **1468** | 33 | 15W / 0D / 18L |
| 91 | [#122 — [Idea] Perivascular immune-state transitions during chemotherapy response](https://github.com/kayoderaheem/research-portfolio/issues/122) | **1468** | 19 | 8W / 0D / 11L |
| 92 | [#113 — [Idea] Patient-reproducible lineage transitions at minimal residual disease after EGFR inhibition](https://github.com/kayoderaheem/research-portfolio/issues/113) | **1467** | 17 | 7W / 0D / 10L |
| 93 | [#97 — [Idea] Virtual-cell prediction of mechanical recovery and alveolar niche memory](https://github.com/kayoderaheem/research-portfolio/issues/97) | **1467** | 13 | 5W / 0D / 8L |
| 94 | [#18 — [Idea] Spatially resolved metabolic-inflammatory routes to gemcitabine resistance in cholangiocarcinoma](https://github.com/kayoderaheem/research-portfolio/issues/18) | **1467** | 40 | 18W / 1D / 21L |
| 95 | [#103 — [Idea] Pharmacogenomic phenoconversion as a reversible source of apparent targeted-therapy resistance](https://github.com/kayoderaheem/research-portfolio/issues/103) | **1467** | 9 | 3W / 0D / 6L |
| 96 | [#9 — [Idea] Spatially resolved IL-17 and retinoid states predicting tunnel-directed therapy response in hidradenitis suppurativa](https://github.com/kayoderaheem/research-portfolio/issues/9) | **1466** | 44 | 20W / 1D / 23L |
| 97 | [#40 — [Idea] Context-aware virtual screening of apoptosis combinations in germ cell tumors](https://github.com/kayoderaheem/research-portfolio/issues/40) | **1466** | 36 | 16W / 1D / 19L |
| 98 | [#53 — [Idea] Early treatment-decision value of heterogeneity trajectories in HER2-targeted bladder cancer](https://github.com/kayoderaheem/research-portfolio/issues/53) | **1466** | 21 | 9W / 0D / 12L |
| 99 | [#64 — [Idea] Myeloid-primed necrosis trajectories predict STING-agonist response in osteosarcoma](https://github.com/kayoderaheem/research-portfolio/issues/64) | **1466** | 19 | 8W / 0D / 11L |
| 100 | [#128 — [Idea] External clinical-use validation of blood–urine metabolite panels for autism diagnostic triage](https://github.com/kayoderaheem/research-portfolio/issues/128) | **1465** | 7 | 2W / 0D / 5L |
| 101 | [#49 — [Idea] Exposure-adjusted phosphoproteomic signatures of pharmacologic failure versus biological resistance](https://github.com/kayoderaheem/research-portfolio/issues/49) | **1465** | 17 | 7W / 0D / 10L |
| 102 | [#8 — [Idea] Metastatic-site spatial niches that modify ALK-inhibitor response](https://github.com/kayoderaheem/research-portfolio/issues/8) | **1464** | 25 | 11W / 0D / 14L |
| 103 | [#52 — [Idea] Isoform-switching mechanisms that separate intrinsic from acquired drug resistance](https://github.com/kayoderaheem/research-portfolio/issues/52) | **1464** | 15 | 6W / 0D / 9L |
| 104 | [#115 — [Idea] Invasive-front hybrid states and tissue context as predictors of MYC-inhibitor response in pancreatic cancer](https://github.com/kayoderaheem/research-portfolio/issues/115) | **1464** | 9 | 3W / 0D / 6L |
| 105 | [#109 — [Idea] Genome-derived structural resistance markers from FFPE tumors beyond exome sequencing](https://github.com/kayoderaheem/research-portfolio/issues/109) | **1464** | 17 | 7W / 0D / 10L |
| 106 | [#68 — [Idea] Local IL-15 access states as predictors of innate-cell therapy response in brain metastases](https://github.com/kayoderaheem/research-portfolio/issues/68) | **1464** | 17 | 7W / 0D / 10L |
| 107 | [#111 — [Idea] Cell-resolved pharmacodynamic niches predict antisense oligonucleotide treatment response](https://github.com/kayoderaheem/research-portfolio/issues/111) | **1464** | 7 | 2W / 0D / 5L |
| 108 | [#50 — [Idea] Population-calibrated pharmacogenomic prediction of tamoxifen benefit and endocrine resistance](https://github.com/kayoderaheem/research-portfolio/issues/50) | **1464** | 19 | 8W / 0D / 11L |
| 109 | [#96 — [Idea] Counterfactual virtual cells for FGF-driven oligodendrocyte state transitions](https://github.com/kayoderaheem/research-portfolio/issues/96) | **1464** | 17 | 7W / 0D / 10L |
| 110 | [#54 — [Idea] Persistence and specificity of treatment-induced T-cell clones as a response discriminator in checkpoint therapy](https://github.com/kayoderaheem/research-portfolio/issues/54) | **1463** | 17 | 7W / 0D / 10L |
| 111 | [#3 — [Idea] Early detection of DNA-damage-tolerance escape during genotoxic therapy](https://github.com/kayoderaheem/research-portfolio/issues/3) | **1462** | 27 | 12W / 0D / 15L |
| 112 | [#11 — [Idea] Spatially constrained T-cell fitness states predicting blinatumomab response in B-cell leukemia](https://github.com/kayoderaheem/research-portfolio/issues/11) | **1461** | 29 | 12W / 1D / 16L |
| 113 | [#5 — [Idea] Spatially resolved immune-priming trajectories during cervical chemoradiotherapy](https://github.com/kayoderaheem/research-portfolio/issues/5) | **1460** | 22 | 8W / 3D / 11L |
| 114 | [#41 — [Idea] Falsifying resettable virtual-cell models of quiescent chromatin](https://github.com/kayoderaheem/research-portfolio/issues/41) | **1456** | 30 | 13W / 0D / 17L |
| 115 | [#88 — [Idea] Prospective falsification of chromatin-to-expression counterfactuals](https://github.com/kayoderaheem/research-portfolio/issues/88) | **1456** | 16 | 6W / 0D / 10L |
| 116 | [#23 — [Idea] Incremental value of dynamic inflammation for recovery-guided rehabilitation after knee arthroplasty](https://github.com/kayoderaheem/research-portfolio/issues/23) | **1456** | 32 | 14W / 0D / 18L |
| 117 | [#19 — [Idea] Spatially gated ZNF423-stress transitions predicting therapy escape in NF1-associated MPNST](https://github.com/kayoderaheem/research-portfolio/issues/19) | **1450** | 22 | 9W / 0D / 13L |
| 118 | [#4 — [Idea] Reproducible myeloid-niche remodeling as a determinant of metastatic immunotherapy response](https://github.com/kayoderaheem/research-portfolio/issues/4) | **1450** | 27 | 11W / 1D / 15L |
| 119 | [#34 — [Idea] Prospective falsification of a dynamic proteomic virtual cell across unseen therapies and organoid contexts](https://github.com/kayoderaheem/research-portfolio/issues/34) | **1450** | 18 | 7W / 0D / 11L |
| 120 | [#26 — [Idea] Site-robust multimodal risk stratification for fetal growth restriction management](https://github.com/kayoderaheem/research-portfolio/issues/26) | **1450** | 24 | 10W / 0D / 14L |
| 121 | [#46 — [Idea] TET2-mutant clonal-hematopoiesis macrophages as a reversible cause of BRAF/MEK resistance in anaplastic thyroid cancer](https://github.com/kayoderaheem/research-portfolio/issues/46) | **1447** | 12 | 3W / 1D / 8L |
| 122 | [#38 — [Idea] Cross-species identifiability of conserved versus context-specific perturbation responses](https://github.com/kayoderaheem/research-portfolio/issues/38) | **1446** | 17 | 6W / 0D / 11L |
| 123 | [#142 — [Idea] Identifiable resistance-state transfer across differentiation and drug shifts](https://github.com/kayoderaheem/research-portfolio/issues/142) | **1446** | 11 | 3W / 0D / 8L |
| 124 | [#32 — [Idea] Clinical-use validation of multimodal myocarditis triage for immunotherapy and intensive monitoring](https://github.com/kayoderaheem/research-portfolio/issues/32) | **1446** | 25 | 10W / 0D / 15L |
| 125 | [#143 — [Idea] Falsifiable virtual-cell test of enhancer-memory counterfactuals](https://github.com/kayoderaheem/research-portfolio/issues/143) | **1445** | 11 | 3W / 0D / 8L |
| 126 | [#124 — [Idea] Population- and site-calibrated multimodal prediction of anti-tuberculosis drug-induced liver injury](https://github.com/kayoderaheem/research-portfolio/issues/124) | **1444** | 7 | 1W / 0D / 6L |
| 127 | [#79 — [Idea] Pathogen-aware multimodal calibration for pulmonary sepsis treatment selection](https://github.com/kayoderaheem/research-portfolio/issues/79) | **1444** | 13 | 4W / 0D / 9L |
| 128 | [#146 — [Idea] Prospectively falsifiable SPDEF genotype-by-stress virtual cells](https://github.com/kayoderaheem/research-portfolio/issues/146) | **1443** | 7 | 1W / 0D / 6L |
| 129 | [#74 — [Idea] Site-calibrated maternal-placental-fetal multimodal risk stratification for neonatal immune-metabolic follow-up](https://github.com/kayoderaheem/research-portfolio/issues/74) | **1443** | 13 | 4W / 0D / 9L |
| 130 | [#110 — [Idea] Endpoint concordance of histologic, imaging, and circulating response signals in osteosarcoma neoadjuvant therapy](https://github.com/kayoderaheem/research-portfolio/issues/110) | **1442** | 7 | 1W / 0D / 6L |
| 131 | [#59 — [Idea] Spatial access states that determine engineered T-cell treatment response](https://github.com/kayoderaheem/research-portfolio/issues/59) | **1441** | 15 | 5W / 0D / 10L |
| 132 | [#82 — [Idea] Clinical-use validation of multimodal GFAP trajectory monitoring in pediatric Alexander disease](https://github.com/kayoderaheem/research-portfolio/issues/82) | **1440** | 15 | 5W / 0D / 10L |
| 133 | [#62 — [Idea] Reproducible tumor–lung interface ERK adaptation after MCL1 inhibition](https://github.com/kayoderaheem/research-portfolio/issues/62) | **1440** | 29 | 12W / 0D / 17L |
| 134 | [#29 — [Idea] Defining a clinical-use pathway for urine microRNA as an incremental toxicity biomarker in prostate SBRT](https://github.com/kayoderaheem/research-portfolio/issues/29) | **1434** | 22 | 8W / 0D / 14L |
| 135 | [#125 — [Idea] Mechanically calibrated multimodal phenotyping for personalized osteoarthritis load management](https://github.com/kayoderaheem/research-portfolio/issues/125) | **1422** | 11 | 2W / 0D / 9L |
| 136 | [#107 — [Idea] Flux-constrained metabolic response signatures across tumor sampling contexts](https://github.com/kayoderaheem/research-portfolio/issues/107) | **1419** | 11 | 2W / 0D / 9L |
| 137 | [#44 — [Idea] Early functional detection of hypoxia-mediated resistance before radiographic treatment failure](https://github.com/kayoderaheem/research-portfolio/issues/44) | **1419** | 23 | 8W / 0D / 15L |
| 138 | [#94 — [Idea] Paracrine-aware virtual cells for engineered astrocyte perturbations](https://github.com/kayoderaheem/research-portfolio/issues/94) | **1418** | 15 | 4W / 0D / 11L |
| 139 | [#22 — [Idea] Transportable validation of a therapy-responsive pathogenic immune state in multiple sclerosis](https://github.com/kayoderaheem/research-portfolio/issues/22) | **1413** | 19 | 6W / 0D / 13L |
| 140 | [#58 — [Idea] Reproducible IFN-response trajectories that separate immune execution from adaptive escape](https://github.com/kayoderaheem/research-portfolio/issues/58) | **1407** | 16 | 4W / 0D / 12L |
| 141 | [#72 — [Idea] Clinical-use validation of YTHDC1 condensate state as a treatment-selection biomarker for METTL3 inhibition](https://github.com/kayoderaheem/research-portfolio/issues/72) | **1400** | 17 | 4W / 0D / 13L |
| 142 | [#47 — [Idea] Cross-cancer validation of lactate-transport states as predictors of drug-tolerant persistence](https://github.com/kayoderaheem/research-portfolio/issues/47) | **1395** | 15 | 3W / 0D / 12L |
| 143 | [#6 — [Idea] Mechanical-niche states that forecast glioblastoma radioresistance](https://github.com/kayoderaheem/research-portfolio/issues/6) | **1386** | 20 | 5W / 0D / 15L |
| 144 | [#21 — [Idea] Decision-value thresholds for multimodal treatment matching in opioid use disorder](https://github.com/kayoderaheem/research-portfolio/issues/21) | **1385** | 17 | 3W / 0D / 14L |
| 145 | [#12 — [Idea] Antigen-presentation escape neighborhoods predicting checkpoint response in melanoma with HIV](https://github.com/kayoderaheem/research-portfolio/issues/12) | **1367** | 16 | 2W / 0D / 14L |
| 146 | [#95 — [Idea] Evolution-aware virtual cells for unseen therapy resistance states](https://github.com/kayoderaheem/research-portfolio/issues/95) | **1365** | 12 | 0W / 0D / 12L |

_Last synchronized: 2026-11-25 19:22 UTC._
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
