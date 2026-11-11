# Research Idea Card

## Working title
Patient-level tissue-context gain over composition for multimodal lymphoma treatment-response prediction

## Observation
Multimodal AI studies in DLBCL have combined PET/CT, digital pathology, molecular data, and clinical variables, yet externally validated prognostic gain over established baselines such as the International Prognostic Index has been inconsistent; treatment-response models are still largely retrospective or exploratory.

## Scientific problem
The field lacks a leakage-resistant benchmark that isolates whether spatial tissue context contributes reproducible treatment-response signal beyond cell composition and established clinical covariates.

## Gap
Without patient-level and center-level validation of nested baselines, complex multimodal models may capture cohort, center, or sampling artifacts instead of transportable biology.

## Research question
Does adding spatial relationships among malignant, immune, and stromal states improve calibrated treatment-response prediction over composition, imaging, molecular, and clinical baselines in lymphoma?

## Hypothesis
Spatial organization provides a modest but reproducible external gain, especially through treatment-induced remodeling patterns, while part of the apparent performance of high-complexity multimodal models disappears under strict patient-level and center-held-out evaluation.

## Data
Multicenter lymphoma cohorts with pretreatment tissue, spatial or digital pathology data, cell-type annotations or single-cell references, available imaging and molecular variables, treatment metadata, response outcomes, follow-up, and a prespecified independent external validation cohort.

## Method to borrow or adapt
Preregistered nested benchmark with patient-level independence: compare nested model families (clinical only; clinical plus composition; imaging/molecular; imaging/molecular plus spatial context) under identical preprocessing, tuning budgets, missing-data handling, calibration strategy, and center-held-out external validation.

## Why this method fits the biology
The central claim is incremental information from tissue organization rather than abundance alone, so fair nested comparisons and spatial negative controls are required to separate biologically meaningful context from burden- or center-driven proxies.

## Strong baselines
- Clinical covariates including International Prognostic Index
- Clinical covariates plus tumor and immune/stromal composition
- Digital pathology-only or imaging-only established baseline
- Penalized regression using prespecified molecular and composition features
- Mean-prediction and prevalence-matched negative controls
- Spatially shuffled and region-matched spatial negative controls

## Primary validation
Use nested patient-level cross-validation for development, then evaluate a locked model on an independent external cohort and a center-held-out split; report calibrated discrimination, confidence intervals, decision curves, subgroup performance, uncertainty, missingness, and abstention rates.

## Biological contribution
Quantifies whether tissue spatial context carries reproducible response information beyond composition and clinical covariates, and identifies which spatial features remain stable enough to justify prospective measurement.

## Novelty claim
A preregistered, leakage-controlled, patient-level and center-level benchmark of incremental spatial-context value for lymphoma treatment-response prediction across multimodal inputs.

## Biggest assumption
Response labels and assessment timing can be harmonized sufficiently across cohorts to support fair external and center-held-out comparisons.

## Cheapest discriminating test
In a multicenter retrospective cohort with one center held out, test whether adding locked spatial-context features improves externally evaluated calibrated discrimination by at least 0.05 over the composition-plus-clinical baseline, with confidence intervals excluding no gain.

## Go / No-Go criterion
Go if spatial context shows reproducible external gain and stable held-out-center calibration; no-go or pivot if gains collapse under center-held-out evaluation or spatial negative controls.

## Target venues
Blood, Journal of Clinical Oncology, Nature Medicine, npj Digital Medicine

## Estimated execution class
`moderate`

## Source papers
- https://doi.org/10.9734/jamps/2026/v28i10893
- https://doi.org/10.1093/bioinformatics/btag680
- https://doi.org/10.1038/s41746-026-03238-5
