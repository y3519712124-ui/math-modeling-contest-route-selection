# Award-Style Question Decomposition

Use this file when a task asks how national-award, first-prize, or excellent mathematical modeling papers reason through the sub-questions inside one problem.

## Evidence Boundary

This is an archetype guide, not a claim that every historical paper has been exhaustively processed. Treat it as a distilled pattern from official contest archives, public excellent-paper collections, and recurring high-performing paper structures.

Prefer phrasing such as:

- "In award-style papers, this sub-question usually plays the role of..."
- "This resembles the mechanism/optimization/evaluation archetype."
- "A strong route would build the baseline first, then add..."

Avoid phrasing such as:

- "All national-award papers did..."
- "The 40-year corpus proves..."
- "Judges always prefer..."

## Role-Based Question Chain

Do not force every problem into Q1/Q2/Q3/Q4. CUMCM and MCM/ICM problems vary in sub-question count and sometimes merge roles.

Use roles first, then map the actual question numbers.

| Role | Typical position | Modeling purpose | Strong-paper signal |
| --- | --- | --- | --- |
| `first` | Q1 | Understand the object, clean data, estimate parameters, build a baseline, or solve a simplified case. | A result exists by day one and gives a benchmark. |
| `main` | Q2 or central question | Build the main model, optimization, prediction, evaluation, mechanism, or algorithm. | The method directly changes the required decision/output. |
| `extend` | middle or penultimate question | Add uncertainty, scenarios, constraints, robustness, sensitivity, or generalization. | The paper proves the main model is not fragile. |
| `final` | last question | Convert results into recommendations, final ranking, implementation plan, generalized method, or policy conclusion. | The paper closes the loop from model to decision. |

Mapping rule:

- 1 sub-question: treat it as `main` and `final`.
- 2 sub-questions: `first`, `final`.
- 3 sub-questions: `first`, `main`, `final`; merge robustness into either main validation or final sensitivity.
- 4+ sub-questions: `first`, `main`, one or more `extend`, `final`.

## Universal Award-Style Pattern

For every sub-question, fill the chain:

1. Required deliverable: what must be calculated, predicted, ranked, optimized, explained, or recommended?
2. Baseline: what simple result can be obtained quickly?
3. Upgrade: what problem-specific modeling layer fixes the baseline's weakness?
4. Solver: how will it be computed and checked within contest time?
5. Validation: what comparison, sensitivity, ablation, limiting case, or external consistency check applies?
6. Figure/table: what will the judge see?
7. Fallback: what can still be submitted if the upgrade fails?
8. Dependency: how does this answer feed the next sub-question or final conclusion?

If a sub-question has no baseline, no validation, and no visible output, it is probably a prose section rather than a model.

## Archetype Decompositions

### Mechanism, Physics, And Engineering

Strong thinking:

- `first`: define variables, units, geometry, conservation relation, or simplified mechanism.
- `main`: build calibrated equations, numerical simulation, or parameter-estimation model.
- `extend`: test limiting cases, perturb uncertain parameters, or add medium/geometry corrections.
- `final`: produce design rules, parameter ranges, error bounds, or operational recommendations.

Baseline:

- Dimensional analysis, closed-form simplification, or one-factor simulation.

Upgrade:

- Mechanism equation plus calibration, finite-difference simulation, constrained fitting, or hybrid mechanism-statistical correction.

Validation:

- Unit checks, limiting cases, residual plots, convergence, sensitivity bands.

Common AI mistake:

- Writing impressive equations without proving units, parameters, or deliverables match the question.

Fallback:

- Submit the simplified mechanism with bounded parameters and sensitivity plots.

### Optimization, Scheduling, Allocation, And Logistics

Strong thinking:

- `first`: define decision variables, feasibility constraints, and a greedy or relaxed baseline.
- `main`: formulate objective and constraints; solve exact small cases and scalable large cases.
- `extend`: add robustness, uncertainty, scenarios, fairness, capacity, or multi-objective tradeoffs.
- `final`: recommend a plan and explain tradeoffs with tables and maps.

Baseline:

- Greedy rule, shortest path, assignment, LP relaxation, or current-policy simulation.

Upgrade:

- MILP, network flow, dynamic programming, robust optimization, or simulation-optimization.

Validation:

- Constraint satisfaction, exact-small-case comparison, heuristic gap, convergence, sensitivity to weights/capacity.

Common AI mistake:

- Using a metaheuristic with no exact small-case check or no reason its objective matches the deliverable.

Fallback:

- Use deterministic heuristic plus local improvement and clearly report the tradeoff gap.

### Forecasting And Time Series

Strong thinking:

- `first`: clean series, define target, build naive/moving-average/exponential-smoothing baseline.
- `main`: add trend, seasonality, shocks, mechanism features, or external covariates.
- `extend`: evaluate scenario errors, rolling-window stability, or decision regret.
- `final`: convert forecasts into capacity, resource, risk, or policy decisions.

Baseline:

- Naive last-value, seasonal naive, moving average, or exponential smoothing.

Upgrade:

- ARIMA/state-space, gradient boosting with domain features, hybrid mechanism features, or uncertainty intervals.

Validation:

- Rolling-origin validation, residual diagnostics, interval coverage, decision-regret comparison.

Common AI mistake:

- Reporting accuracy without showing how forecast error changes the final decision.

Fallback:

- Use simple baseline plus uncertainty intervals and scenario decisions.

### Evaluation, Ranking, And Comprehensive Assessment

Strong thinking:

- `first`: define alternatives, indicators, directionality, normalization, and a transparent baseline ranking.
- `main`: justify weights and aggregation with mechanism, data variation, expert logic, or dominance relations.
- `extend`: perturb weights, test rank stability, compare methods, or cluster alternatives before ranking.
- `final`: recommend tiers, intervention priorities, or improvement paths.

Baseline:

- Normalized indicator table, equal-weight score, dominance/Pareto relation, or PCA projection.

Upgrade:

- Entropy/AHP/TOPSIS/fuzzy method only after indicators and weights are defensible.

Validation:

- Weight perturbation, rank correlation, known-case check, ablation of indicators.

Common AI mistake:

- AHP/entropy/TOPSIS stack with arbitrary indicators and no rank stability.

Fallback:

- Equal-weight/Pareto baseline with stability analysis and qualitative interpretation.

### Graph, Network, And Complex Systems

Strong thinking:

- `first`: define nodes, edges, weights, and baseline topology metrics.
- `main`: model flow, spread, intervention, shortest path, centrality, or cascading risk.
- `extend`: simulate targeted failure, protection, subsidy, congestion, or uncertainty in edges.
- `final`: identify critical nodes/edges and justify intervention priorities.

Baseline:

- Degree, shortest path, centrality, connectivity, or simple SIR/logistic spread.

Upgrade:

- Weighted/multilayer network, Markov chain, flow-aware centrality, network intervention simulation.

Validation:

- Compare topology-only and flow-aware results, stress node/edge removal, reproduce known limiting behavior.

Common AI mistake:

- Building a network because it looks modern, without problem-specific edges or decision consequences.

Fallback:

- Use interpretable topology metrics plus scenario intervention table.

### Simulation, Agent, And Game Behavior

Strong thinking:

- `first`: identify actor types, state variables, payoffs/rules, and a small deterministic baseline.
- `main`: simulate interactions or equilibrium under calibrated rules.
- `extend`: stress behavior parameters, scenarios, or policy interventions.
- `final`: recommend rules/policies that are stable across plausible behaviors.

Baseline:

- Payoff matrix, queue model, deterministic scenario, or few-agent hand simulation.

Upgrade:

- Agent-based simulation, evolutionary game, Monte Carlo, queuing network, or scenario generator.

Validation:

- Equilibrium plausibility, parameter sensitivity, reproduction of known constraints or simple cases.

Common AI mistake:

- Inventing agent rules with no calibration or limiting-case check.

Fallback:

- Reduce actor types and submit scenario tables with sensitivity.

### Image, Signal, And Data Mining

Strong thinking:

- `first`: define measurable target, preprocessing, quality control, and rule/classical-feature baseline.
- `main`: extract domain features or train a model only when data supports it.
- `extend`: propagate recognition error into the final modeling result.
- `final`: produce classifications, measurements, risk levels, or operational decisions.

Baseline:

- Thresholding, classical features, rule-based extraction, logistic regression, or simple classifier.

Upgrade:

- Random forest/SVM/CNN/segmentation only with cross-validation and error interpretation.

Validation:

- Confusion matrix, ablation, error cases, downstream error propagation.

Common AI mistake:

- Treating model accuracy as the final answer when the contest asks for a decision or measurement.

Fallback:

- Use classical interpretable features and report uncertainty/error propagation.

### Compositional, Chemical, And Percentage-Sum Data

Use this for oxide percentages, chemical ingredients, glass composition, soil nutrient proportions, or any variables constrained by a fixed total.

Strong thinking:

- `first`: clean missing/invalid components, check whether percentages sum to a constant, and build raw-percentage descriptive baseline.
- `main`: use closed-sum-aware features such as component ratios, CLR/ILR transforms, or interpretable log-ratio coordinates before clustering/classification.
- `extend`: add correction/recovery for weathering, corrosion, loss, or measurement drift; compare corrected and uncorrected models.
- `final`: report class rules, unknown-sample predictions, and component patterns that remain stable under transform and correction choices.

Baseline:

- Raw component statistics, boxplots, chi-square/t-tests, and raw-percentage PCA/clustering.

Upgrade:

- Log-ratio transform plus closed-sum-aware clustering/discriminant, weathering correction, and interpretable component-ratio rules.

Validation:

- Raw versus log-ratio ablation, corrected versus uncorrected classification, known unweathered sample recovery, bootstrap stability, confusion matrix.

Common AI mistake:

- Running PCA/K-means/Fisher directly on raw percentages and treating closed-sum artifacts as chemical structure.

Fallback:

- If log-ratio transforms are unstable because of zeros or missing components, group trace components, add a small justified replacement value, and submit raw baseline plus ratio-based sensitivity.

### Bearing-Only Localization And Geometric Identifiability

Use this for passive localization, direction-of-arrival, pure bearing angles, transmitter selection, formation correction, and geometric adjustment problems.

Strong thinking:

- `first`: solve the well-posed analytic triangulation case and identify mirror-symmetry or multi-solution ambiguity.
- `main`: prove minimum-source or identifiability conditions before optimizing positions.
- `extend`: quantify sensitivity through condition number, GDOP, Jacobian error propagation, confidence ellipse, or Monte Carlo bearing noise.
- `final`: design a robust adjustment strategy and validate convergence, residuals, and improvement over a greedy or naive least-squares baseline.

Baseline:

- Sine/cosine law triangulation or ordinary least squares using known transmitters.

Upgrade:

- Identifiability/minimum-source proof, robust nonlinear least squares, geometry-quality metrics, and error-propagation analysis.

Validation:

- Reverse-check known locations, residual angle errors, mirror-solution rejection, Monte Carlo perturbation bands, convergence curves.

Common AI mistake:

- Presenting a triangulation formula and one simulation example without proving uniqueness or explaining when the geometry becomes unstable.

Fallback:

- If identifiability proof is incomplete by Day 2, enumerate feasible transmitter sets, reject mirror solutions by explicit direction constraints, and report residual/Monte Carlo validation.

### Policy, Environment, Health, And Public Systems

Strong thinking:

- `first`: define stakeholders, measurable outcome, constraints, and descriptive baseline.
- `main`: build evaluation, regression, causal-assumption, resource allocation, or scenario model.
- `extend`: compare policies under equity/cost/uncertainty constraints.
- `final`: recommend practical actions with tradeoffs and implementation limits.

Baseline:

- Descriptive statistics, current-policy simulation, equal allocation, or simple index.

Upgrade:

- Scenario simulation, robust policy selection, interpretable regression, multi-objective optimization, or mechanism-data hybrid.

Validation:

- Sensitivity to assumptions, placebo/known-case checks when possible, external consistency, fairness/cost tradeoff table.

Common AI mistake:

- Broad recommendations unsupported by measurable outputs.

Fallback:

- Scenario comparison with transparent assumptions and feasibility constraints.

## Hybrid Problems

Many strong papers combine two archetypes. Use the primary deliverable to choose the main role template:

- Forecasting + optimization: forecast first, optimize second, validate by decision regret.
- Evaluation + clustering: group first, score within groups, validate by rank stability.
- Mechanism + machine learning: mechanism features first, predictive model second, validate by ablation.
- Network + intervention: build network first, simulate intervention second, validate by scenario stress.
- Simulation + robust decision: generate scenarios first, choose stable policy second.

When archetypes conflict, the `main` role should follow the final decision object, not the most fashionable method.

## C-Type And Data-Oriented Problems

For data-heavy C-type or data-oriented problems, the `first` role is often exploratory data analysis and feature reliability rather than a physical baseline.

Strong C-style chain:

- `first`: clean data, define target, detect missingness/outliers, build descriptive baseline.
- `main`: construct domain features and a predictive/evaluation/classification model.
- `extend`: test robustness by cross-validation, ablation, threshold sensitivity, or subgroup stability.
- `final`: translate outputs into thresholds, rankings, policies, warnings, or decision rules.

Do not choose C only because data exists. Choose it when the team can build non-generic features and validate the final decision.

## Anti-Homogeneity Moves

Use at least one of these in every strong route:

- Baseline-first: show a simple model before the advanced model.
- Route-level ablation: remove the claimed innovation and show what changes.
- Exact-small-case check: solve small cases exactly, then scale with a heuristic.
- Decision regret: measure how forecast/evaluation errors change the decision.
- Rank stability: perturb weights/indicators and show whether rankings survive.
- Uncertainty band: report parameter or scenario intervals rather than one number.
- Limiting-case check: prove the model behaves correctly in obvious edge cases.
- Domain feature: create a feature or variable that comes from the actual problem, not a generic package.

## Sources To Ground Historical Claims

- CUMCM official site: https://www.mcm.edu.cn/
- CUMCM historical problem archive: https://www.mcm.edu.cn/html_cn/node/a53a84ead7b2e5087dc59954d440219a.html
- CUMCM excellent-paper collection, community-organized and non-official: https://www.cmathc.org.cn/mcm/lw/
- COMAP MCM/ICM contest matrix: https://www.contest.comap.com/undergraduate/contests/matrix/index.html
