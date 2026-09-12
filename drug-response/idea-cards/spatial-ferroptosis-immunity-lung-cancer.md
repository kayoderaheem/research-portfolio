# Research Idea Card

## Working title
Spatial ferroptosis-to-immunity transitions during combination therapy in lung cancer

## Observation
Mitochondrial stress can activate cGAS–STING signaling and ferroptosis-linked immune recruitment, while NSCLC subsets show differential ferroptosis sensitivity under ribonucleotide reductase inhibition.

## Scientific problem
It is unclear whether treatment-induced tumor death is spatially coupled to productive local immune activation in a reproducible way across patients.

## Gap
Composition-only assays cannot test whether ferroptotic tumor states are physically and reproducibly connected to activated dendritic-cell and CD8 T-cell neighborhoods.

## Research question
Are reproducible spatial transitions linking ferroptotic tumor cells to dendritic-cell and CD8 T-cell neighborhoods associated with response to ferroptosis-inducing combination therapy across patients?

## Hypothesis
Responders show an early, localized transition from stressed tumor states to ferroptotic tumor states surrounded by activated antigen-presenting and cytotoxic lymphoid cells; nonresponders show uncoupled stress or immune exclusion.

## Data
Matched pretreatment and early on-treatment lung cancer tissue with treatment/response labels, spatial or single-cell transcriptomics, multiplex imaging and/or lipid-peroxidation assays, and immune composition measurements.

## Method to borrow or adapt
Patient-level spatial neighborhood modeling with paired pre/post-treatment profiling, distance-aware coupling scores, and nested cross-validation with leave-one-patient-out replication.

## Why this method fits the biology
The biological claim is explicitly spatial and temporal (ferroptotic tumor states adjacent to activated immune states after therapy), so neighborhood-aware paired modeling is required to distinguish productive local coupling from generic tumor death or baseline immune abundance.

## Strong baselines
- Clinical covariates and treatment-only response model
- Tumor death burden without spatial terms
- Immune composition/activation scores without spatial relationships
- Established proliferation, hypoxia, and interferon pathway scores
- Regularized calibrated regression

## Primary validation
Nested patient-level cross-validation with locked feature discovery/calibration and external replication in an independent cohort or orthogonal spatial assay.

## Biological contribution
Clarifies whether ferroptosis in tissue is an immunologically productive response mechanism versus a tumor-intrinsic death phenotype.

## Novelty claim
Introduces and tests a patient-level spatial coupling mechanism between ferroptotic tumor states and nearby activated dendritic-cell/CD8 neighborhoods under treatment.

## Biggest assumption
Ferroptosis can be robustly distinguished from apoptosis/necrosis and generic stress in tissue-scale measurements.

## Cheapest discriminating test
In paired early-treatment tissue, test whether ferroptosis-marked tumor cells are preferentially adjacent to activated dendritic cells and CD8 T cells in responders after adjusting for death burden and immune composition.

## Go / No-Go criterion
Go if a prespecified spatial coupling score improves held-out patient-level calibration beyond death burden/composition and replicates in an independent cohort or assay; no-go if coupling adds no reproducible signal.

## Target venues
Cancer Discovery, Nature Cancer, Cancer Cell, Cell Reports Medicine

## Estimated execution class
`moderate`

## Source papers
- https://doi.org/10.63808/ghc.v2i1.524
- https://doi.org/10.1158/2767-9764.33618714
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE346380
