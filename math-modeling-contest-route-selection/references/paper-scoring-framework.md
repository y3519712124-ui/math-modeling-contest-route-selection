# Paper Scoring Framework

Use this file when judging whether a modeling route can become a competitive paper, or when the user asks for multi-dimensional scoring standards based on mathematical modeling evaluation practice.

## Evidence Boundary

Official contests publish rules, problem statements, result lists, and in some cases excellent-paper collections, but detailed judge rubrics are rarely public as a single universal formula. Treat this framework as an operational scoring proxy for contest preparation, not as an official scoring sheet.

## Scoring Dimensions

Score each dimension from 0 to 5.

| Dimension | Weight | What judges can see |
| --- | ---: | --- |
| deliverable_alignment | 0.14 | The paper answers exactly what each sub-question asks for. |
| assumption_quality | 0.10 | Assumptions are necessary, testable, and stress-checked. |
| model_fit_and_originality | 0.16 | The model is problem-specific and improves on a baseline. |
| solution_correctness | 0.12 | Equations, algorithms, constraints, and computations are reproducible. |
| validation_strength | 0.14 | Baseline comparison, sensitivity, ablation, external check, or limiting case exists. |
| decision_value | 0.12 | Results change a recommendation, policy, plan, ranking, or design choice. |
| paper_expression | 0.10 | Figures, tables, algorithm boxes, and structure make the route easy to judge. |
| engineering_feasibility | 0.07 | The route can be implemented, debugged, and rerun during contest time. |
| differentiation | 0.05 | The paper avoids generic AI-style method stacking. |

Use this as a paper-competitiveness lens after a plausible topic and route exist. Do not let it replace topic feasibility checks.

## Observable Score Anchors

### 5-Point Signal

- Each sub-question has a baseline, main model, validation, and visible result.
- The model has one clear problem-specific idea.
- The paper compares against a simpler method and explains what changes.
- The model-choice section names at least one rejected alternative and the test used to reject it.
- Assumptions are tested by sensitivity, limiting cases, or scenario stress.
- Figures/tables support the claims without requiring long prose.

### 3-Point Signal

- The method is plausible but generic.
- Validation exists but is thin or mostly qualitative.
- Results answer the problem, but the superiority over simpler routes is unclear.
- Some assumptions are listed but not stress-tested.

### 1-Point Signal

- The paper mainly lists methods.
- No baseline exists.
- Data, parameters, or weights are arbitrary.
- The final answer is a descriptive summary, not a decision.
- Figures are decorative rather than evidential.

## Pre-Selection Vs Paper-Writing

Use different standards at different times.

Pre-selection scoring should focus on what can be known before solving:

- deliverable clarity
- data/parameter access
- day-one baseline feasibility
- main-model fit
- validation opportunity
- engineering risk
- differentiation opportunity

Paper-writing scoring should focus on what the solution has actually proven:

- validation coverage per sub-question
- result correctness
- figure/table quality
- final recommendation strength
- reproducibility
- sensitivity and ablation evidence

Avoid false precision. If a criterion depends on experiments not yet run, score the opportunity and state the condition that could flip the score.

## Anti-AI-Homogeneity Indicators

Downgrade differentiation when a paper shows these observable patterns:

- Method names appear before variables, deliverables, or constraints.
- AHP/entropy/TOPSIS/grey/LSTM/random forest are used without problem-specific features or validation.
- A model is chosen because it sounds advanced, with no rejected alternative or deciding test.
- Assumption tables contain generic statements that could fit any problem.
- Sensitivity analysis changes arbitrary weights but not the final decision.
- No baseline is presented, so the "advanced" method has nothing to beat.
- Figures are only workflow charts or generic line charts, not evidence for a modeling claim.

Upgrade differentiation when the paper includes:

- a domain-specific variable, feature, constraint, or metric
- a baseline-to-upgrade comparison
- a route-level ablation
- a model-choice tournament that compares baseline, rejected alternative, and chosen route
- an exact-small-case check or limiting-case proof
- uncertainty bands, rank stability, or decision-regret analysis

## Near-Tie Calibration

For 0-5 scoring:

- Difference <= 0.05: near tie; choose by team strengths and problem familiarity.
- Difference <= 0.20: moderate uncertainty; do not call the lead decisive without written evidence.
- Difference > 0.20: meaningful only if decisive criteria have evidence and flip conditions.

For 100-point paper competitiveness scoring:

- Difference <= 3 points: near tie.
- Difference <= 6 points: moderate uncertainty.
- Difference > 6 points: meaningful only with evidence from validation, feasibility, and deliverable alignment.

Tie-break sequence:

1. Can Q1 produce a credible day-one baseline?
2. Does the main question have a problem-specific upgrade rather than a generic method?
3. Is validation stronger than "looks reasonable"?
4. Can the final answer become clear figures/tables and recommendations?
5. Does the route match the team's coding and domain strengths?

## Paper Structure Checklist

Before choosing a route as the primary paper route, verify:

- Abstract can state the baseline, main upgrade, validation, and final decision in one paragraph.
- Assumption section lists only assumptions used later.
- Symbol table matches equations and code variables.
- Each sub-question has a result table or figure.
- The main model section explains why the baseline is insufficient.
- The route states why the chosen model survives refutation and what condition would make it fail.
- Validation appears before recommendations, not as an afterthought.
- Sensitivity analysis changes meaningful parameters.
- Conclusion names the actionable decision and its conditions.

## Red Flags By Section

| Section | Red flag | Rescue |
| --- | --- | --- |
| Problem restatement | Repeats the statement without identifying deliverables. | Add a deliverable table for each sub-question. |
| Assumptions | Too many broad assumptions. | Keep only assumptions needed by equations/data. |
| Model | Advanced method has no baseline. | Add a simple baseline and compare. |
| Solver | Random/metaheuristic result has no reproducibility. | Fix seed, show convergence, compare exact small cases. |
| Data | Cleaning choices are invisible. | Show missing/outlier handling and feature definitions. |
| Validation | Only says results are reasonable. | Add sensitivity, ablation, external check, or limiting case. |
| Results | Tables do not answer decisions. | Convert metrics into rankings, policies, thresholds, or plans. |
| Recommendations | Generic policy prose. | Tie each recommendation to a model result and condition. |

## Sources To Ground Claims

- CUMCM official site: https://www.mcm.edu.cn/
- CUMCM historical problem archive: https://www.mcm.edu.cn/html_cn/node/a53a84ead7b2e5087dc59954d440219a.html
- COMAP MCM/ICM contest matrix: https://www.contest.comap.com/undergraduate/contests/matrix/index.html
