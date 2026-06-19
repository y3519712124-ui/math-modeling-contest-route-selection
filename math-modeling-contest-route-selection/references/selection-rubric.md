# Topic And Method Route Selection Rubric

Use this rubric to rank CUMCM A/B/C candidate problems and their modeling routes. The final recommendation should be route-led: a problem is only strong if at least one modeling route is feasible, validated, and paper-worthy.

## Evidence Boundary

This rubric is an operational contest-preparation proxy, not an official judge scoring sheet. Use it to make topic and route comparisons explicit, auditable, and less AI-homogeneous. When evidence is missing, score the opportunity and state what condition could flip the score.

By default, `scripts/score_topics.py` blends topic score and best-route score as topic 45% and route 55%. This reflects the skill's rule that a good topic is only strong when its executable modeling route is strong.

## Default Topic Criteria

Score each criterion from 0 to 5.

| Criterion | Weight | Meaning |
| --- | ---: | --- |
| feasibility | 0.18 | Can the team finish models, code, figures, and paper in time? |
| data_or_parameter_access | 0.14 | Are data, parameters, or defensible assumptions available? |
| differentiation | 0.18 | Can the solution avoid generic AI similarity and show a clear angle? |
| validation_strength | 0.16 | Can results be tested, compared, or stress-checked? |
| method_fit | 0.12 | Do methods naturally answer the problem rather than decorate it? |
| narrative_power | 0.10 | Can the paper tell a compact, convincing story? |
| risk_control | 0.12 | Are fallback models and failure plans available? |

## Default Method Route Criteria

Score each candidate route from 0 to 5.

| Criterion | Weight | Meaning |
| --- | ---: | --- |
| route_problem_fit | 0.16 | Does the route directly answer the problem's required output? |
| engineering_solvability | 0.16 | Can the team implement, debug, and run the route during the contest? |
| data_parameter_control | 0.14 | Are inputs available, estimable, or defensibly assumed? |
| validation_design | 0.14 | Is there a concrete baseline, sensitivity, ablation, or external check? |
| route_differentiation | 0.14 | Does the route avoid generic AI method stacking? |
| paper_explainability | 0.10 | Can the route be explained with clear equations, algorithm steps, and figures? |
| implementation_cost_control | 0.08 | Is runtime/coding complexity controlled? |
| fallback_robustness | 0.08 | Can a simpler route still produce a complete paper? |

High route scores require more than method names. A route scored 3.8 or above should include `model_choice_rationale`, `rejected_alternatives`, and `refutation_tests` so the score reflects a survived model-choice tournament.

## Optional Question-Chain Criteria

Use this section only when the problem statement has sub-questions and the user asks for per-question modeling logic, paper planning, or national-award-style decomposition. Do not require these scores for quick A/B/C selection.

### Pre-Selection Question-Chain Scores

Score what can be judged before solving.

| Criterion | Weight | Meaning |
| --- | ---: | --- |
| role_alignment | 0.18 | Is each sub-question mapped to a useful role (`first`, `main`, `extend`, `final`) rather than a fixed Q1-Q4 template? |
| deliverable_clarity | 0.18 | Does each sub-question have a measurable output, decision, ranking, prediction, or explanation target? |
| baseline_to_upgrade_logic | 0.22 | Does the route move from a day-one baseline to one justified problem-specific upgrade? |
| dependency_structure | 0.14 | Does each answer feed the next sub-question or final conclusion? |
| validation_opportunity | 0.16 | Is there a plausible comparison, sensitivity, ablation, limiting case, or external check for the chain? |
| fallback_completeness | 0.12 | Can the paper still be complete if the main upgrade fails? |

### Paper-Writing Checklist

Use this after results exist. Do not treat it as precise pre-contest scoring unless evidence is available.

- Every sub-question has at least one result table or figure.
- Q-first has a baseline, parameter estimate, simplified case, or data-quality result.
- Q-main has a model that directly changes the required deliverable.
- Q-main explains why the chosen model beats at least one simpler or common alternative.
- Q-extend, if present, tests robustness, scenarios, uncertainty, or generalization.
- Q-final converts model outputs into recommendations, ranking, design rules, or an implementation plan.
- Validation appears before final recommendations.
- Sensitivity changes meaningful parameters, not arbitrary decorative weights.
- The conclusion states the conditions under which the recommendation remains valid.

## Interpretation

- 4.2-5.0: strong primary choice.
- 3.6-4.2: viable if the team likes the domain and has a clear differentiation layer.
- 3.0-3.6: fallback only; identify one major weakness before choosing.
- below 3.0: avoid unless the team has special expertise or data.

## Red Flags

Downgrade a candidate if:

- The only possible plan is a generic method list.
- The data source is imaginary or too slow to acquire.
- Validation is limited to "the curve looks reasonable."
- The problem requires too much domain knowledge for the team.
- The final answer cannot be turned into figures/tables that judges can inspect quickly.
- The paper would need many pages of assumptions before any useful result appears.
- The best route has no day-one baseline.
- The strongest method is too hard to implement and has no fallback.
- Validation depends only on subjective explanation.
- The chosen model has no rejected alternative or refutation test.
- The route cannot state what evidence would make a simpler baseline preferable.

## Score Calibration Rules

Use these rules when a model produces score tables for A/B/C.

- Do not separate two strong candidates by more than 0.2 points unless the report gives route-level evidence for the gap.
- Treat gaps of about 0.2 or less as moderate unless every decisive criterion has a written reason; manual 0.1-step scoring can easily move the ranking.
- If the top two final scores differ by 0.05 or less, label the result as a near tie and choose by team strengths.
- A route with a day-one baseline can receive 5/5 for baseline feasibility, but its strong-route engineering score should stay below 5/5 unless the report includes solver details, unit checks, and validation evidence.
- A data-analysis topic should not be downgraded as "generic" until a strong non-generic route has been attempted. For NIPT-style topics, evaluate time-to-threshold modeling, calibration, risk curves, and threshold sensitivity before scoring it as low-differentiation.
- A compositional/percentage-sum data topic should not be scored as low-differentiation until a log-ratio-aware or closed-sum-aware route has been considered and rejected.
- A bearing-only/geometric localization topic should not be scored as low-differentiation until identifiability, minimum-source conditions, error propagation, and residual validation have been considered.
- Every decisive topic or route score must include criterion-specific evidence and one condition that could flip that criterion; a single overall evidence sentence should not clear all decisive scores.
- Every primary recommendation must include the strongest reason to reject it and the test that lets it survive.
- Do not award high `route_differentiation` for using an advanced model unless the route shows what simpler or fashionable alternative was rejected and why.
- Do not award high `differentiation` to a crowded/popular topic unless the report separates topic differentiation from route differentiation and names a `crowd_escape_mechanism`.
- If `route_differentiation` is high while topic differentiation is low or moderate, still name the `crowd_escape_mechanism`; a strong route claim is not self-evident to judges.
- If the top candidates fit different team strengths, use `team_fit_score` or an explicit team-fit note instead of hiding the dependency in prose.
- For any constrained optimization, physics, engineering, logistics, or capacity-planning route, require a `binding_constraints` inventory before awarding high route fit, feasibility, or validation scores.

## Physics/Data Route Audit Triggers

For physics or signal-processing topics, require a unit and assumption checklist before awarding high feasibility or validation scores:

- Are units consistent across wavelength, wavenumber, time, distance, or thickness?
- Are angle corrections and medium changes handled explicitly?
- Are simplified and higher-fidelity models separated?
- Is there a residual, sensitivity, or limiting-case check?
- Are binding mechanical/geometric constraints enumerated, including stroke, spacing/deformation, boundary, collision, capacity, or conservation limits?

For biomedical or statistical decision topics, require a calibration and decision-risk checklist:

- Is the prediction target aligned with the decision target?
- Are repeated measurements handled correctly?
- Are thresholds calibrated and stress-tested?
- Is the model framed as statistical association unless causal evidence exists?

For compositional or chemical percentage data, require a closed-sum checklist:

- Do the variables sum to a constant or near-constant total?
- Is raw-percentage PCA/clustering compared with log-ratio or ratio-based features?
- Are zeros, missing values, and trace components handled explicitly?
- Is any weathering/correction model validated by corrected-vs-uncorrected ablation?

For bearing-only localization topics, require an identifiability checklist:

- Is mirror symmetry or multi-solution ambiguity addressed?
- Is the minimum transmitter/source count justified by geometry, not only examples?
- Are condition number, GDOP, Jacobian error propagation, or Monte Carlo angle-noise bands used to stress the geometry?
- Is the adjustment strategy compared with naive least squares or greedy correction?

## Superiority Comparison Template

Use this table in final recommendations:

| Candidate | Best route | Route score | Main highlight | Main risk | Validation path | Final score |
| --- | --- | ---: | --- | --- | --- | ---: |

For the chosen topic, add:

- Why not the obvious/generic route?
- What makes the route escape the crowd on a popular topic?
- What team strengths are assumed, and what team profile would flip the choice?
- What alternative model was rejected, and by what test?
- What baseline will be beaten?
- What ablation proves the differentiated layer matters?
- What figure will make the highlight visible?
- What fallback still yields a complete paper?
