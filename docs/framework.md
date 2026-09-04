# Problem choice for computational biology

This document explains how the portfolio translates Michael A. Fischbach's problem-choice framework into a working system for bioinformatics and precision medicine.

It is an independent adaptation. It does not reproduce the paper's figures and is not affiliated with Michael Fischbach, Stanford University, or *Cell*.

## Intellectual foundation

The source commentary argues that project choice deserves far more time because the importance of the selected problem constrains the eventual impact of even excellent execution. It proposes structured idea generation, explicit impact and success estimates, assumption analysis, early go/no-go experiments, flexibility about fixed parameters, and regular movement between execution and critical re-evaluation.

Primary source:

> Fischbach MA. Problem choice and decision trees in science and engineering. *Cell*. 2024;187(8):1828-1833. <https://doi.org/10.1016/j.cell.2024.03.012>

A public overview is available from [Stanford Engineering](https://engineering.stanford.edu/news/how-pick-and-solve-next-great-problem).

## How the portfolio implements the framework

| Source principle | Portfolio implementation | Bioinformatics extension |
|---|---|---|
| Spend more time choosing | Multiple open candidate issues are compared before commitment | Compare biological questions before choosing an architecture |
| Use prompts to generate ideas | Quick and deep issue forms make ideation concrete | Prompts span perturbation, measurement, computation, and translation |
| Define impact | Each idea states its optimization function | Separate discovery impact, technical utility, and patient value |
| Evaluate likelihood of success | Every idea records an assumption chain, risk, and time-to-readout | Separate biological reality from data and tool capability |
| Fix one parameter | Each idea names one fixed anchor and several floating choices | Keep the question fixed while model, modality, cohort, and endpoint compete |
| Test risk early | Each idea specifies the cheapest discriminating test | Require leakage audits, simple baselines, and small external tests before scale |
| Navigate a decision tree | Continue, refine, pivot, park, and stop branches are written in advance | Negative computational results become evidence about identifiability or transportability |
| Alternate execution and evaluation | Review checkpoints ask what changed and what was learned | Revisit the plan when data, methods, or clinical context changes |

## Impact functions

Different projects should not be judged by one vague definition of impact.

### Discovery science

- How much could be learned?
- How general could the biological insight be?
- Would the result distinguish among plausible mechanisms?

### Technology development

- How broadly could the capability be used?
- Is it critical or difficult to replace for an important application?
- Does it enable a question that existing methods cannot answer?

### Precision medicine

- Could the result improve a real decision for a defined patient population?
- Is the intended use clear enough to determine acceptable error and uncertainty?
- Can the claim survive changes in institution, population, assay, and time?
- Is there a plausible path from retrospective association to prospective utility?

## Assumption analysis

List every assumption connecting the starting data to the final claim. For each assumption, record:

1. **Type:** underlying biological reality or current technical capability.
2. **Risk:** low, medium, or high.
3. **Time-to-readout:** when evidence could confirm or weaken it.
4. **Test:** the cheapest credible way to change confidence.
5. **Branch:** what happens if the assumption holds, is ambiguous, or fails.

A project with several high-risk assumptions that only read out near the end should be redesigned. The aim is not to remove all risk; low-risk projects can be unimportant. The aim is to expose risk and bring informative readouts forward.

## Bioinformatics quality gates

Before a project is promoted from candidate to active, it should answer:

- Is the unit of independence the patient, donor, specimen, image, or cell?
- Are all preprocessing, feature selection, tuning, and imputation steps isolated from the final test data?
- Are splits resistant to donor, batch, site, temporal, and near-duplicate leakage?
- Are the strongest simple and established baselines included?
- Is performance reported with uncertainty rather than only a point estimate?
- Are calibration and clinically relevant decision thresholds evaluated when predictions affect care?
- Are subgroup performance and distribution shifts examined without overstating underpowered results?
- Does an independent cohort or orthogonal assay test the central claim?
- Can the proposed measurements identify the biological mechanism being claimed?
- What negative result would stop optimization?

## Decision vocabulary

- **Continue:** the key assumption survived; scale only after freezing the next claim and validation rule.
- **Refine:** a useful effect appears under narrower conditions; change one floating parameter.
- **Pivot:** the original assumption failed but revealed a stronger question or reversed framing.
- **Park:** the question remains valuable but the required data, capability, or timing is not ready.
- **Stop:** the central claim is weak, unidentifiable, redundant, or insufficiently consequential.

Every branch should record the evidence that triggered it. This keeps a failed approach from becoming lost effort and reduces sunk-cost reasoning.
