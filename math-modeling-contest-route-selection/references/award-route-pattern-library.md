# Award Route Pattern Library

Use this file when the user asks to distill how strong CUMCM, MCM, or ICM papers model and solve each sub-question.

## Evidence Boundary

This is a transfer-pattern library, not a database claiming every winning paper has been read in the current run. The patterns are distilled from official contest archives, public excellent-paper examples, and repeated structures of high-scoring mathematical modeling papers.

Use careful language:

- "Award-style papers often..."
- "This problem resembles the optimization/forecasting/mechanism route..."
- "A strong route would first prove the baseline, then justify the upgrade..."

Avoid:

- "All national prize papers..."
- "The complete 40-year corpus proves..."
- "Judges always..."

## The Core Distillation

Strong papers rarely win because of one advanced algorithm. They win because every sub-question has a visible reasoning chain:

1. Translate the question into a measurable output.
2. Build the smallest baseline that answers it.
3. Identify the baseline's failure mode.
4. Choose one model upgrade that directly fixes that failure.
5. Choose a solver that can finish under contest time.
6. Validate the upgrade against baseline, edge cases, data, or scenarios.
7. Convert results into figures, tables, and decisions.
8. State when the chosen model should be rejected.

The hidden skill is model choice, not model listing.

## Sub-Question Roles In Award Papers

### First Question

Purpose:

- Build trust with a simple, correct result.
- Define variables, units, data quality, feasible set, or baseline behavior.
- Produce the first table or plot by Day 1.

Common modeling choices:

- Mechanism: dimensional analysis, conservation law, simplified ODE/PDE, closed-form case.
- Optimization: greedy rule, relaxation, feasibility model, shortest path, assignment.
- Data: cleaning, descriptive statistics, PCA/visualization, simple regression/classifier.
- Evaluation: equal-weight score, Pareto/dominance relation, transparent index.
- Forecasting: naive, seasonal naive, moving average, exponential smoothing.

Why strong teams choose this:

- It gives a benchmark and exposes whether the data/parameters are usable.
- It protects the paper if the advanced model fails.

Reject the first-question route if:

- It cannot produce a measurable deliverable.
- It uses advanced methods before defining variables or data reliability.
- It does not feed the next question.

### Main Question

Purpose:

- Answer the central required decision: optimize, predict, classify, estimate, simulate, rank, or explain.
- Replace the baseline only after naming its weakness.

Common modeling choices:

- Mechanism upgrade: calibrated equation, numerical simulation, parameter estimation, finite difference.
- Optimization upgrade: MILP, network flow, dynamic programming, robust optimization, simulation-optimization.
- Prediction upgrade: ARIMA/state-space, gradient boosting, random forest, mechanism-feature regression, uncertainty interval model.
- Classification upgrade: logistic regression/SVM/random forest, discriminant analysis, clustering plus interpretable rules.
- Evaluation upgrade: entropy/AHP/TOPSIS/fuzzy/PCA only with justified indicators and stability checks.
- Network upgrade: weighted/multilayer graph, Markov chain, flow-aware centrality, intervention simulation.

Why strong teams choose this:

- The upgrade changes the final decision, not just a score.
- The solver is implementable and has a checkable failure mode.

Reject the main route if:

- The objective does not match the question.
- The model uses a fashionable algorithm without a baseline comparison.
- The solver has no small-case verification or runtime fallback.

### Extend Question

Purpose:

- Prove the main result is not fragile.
- Add uncertainty, scenario, robustness, sensitivity, fairness, capacity, geometry, or policy constraints.

Common modeling choices:

- Parameter sensitivity, Monte Carlo, bootstrap, uncertainty bands.
- Robust optimization, scenario tree, stress test, ablation.
- Rank stability, feature ablation, threshold perturbation.
- Geometry conditioning, error propagation, residual diagnostics.
- Policy scenario comparison and decision-regret analysis.

Why strong teams choose this:

- It converts assumptions into judge-visible evidence.
- It differentiates the paper from generic AI output.

Reject the extend route if:

- It only adds more indicators or models without changing the conclusion.
- It does not test the strongest assumption.
- It has no plot/table that reveals robustness.

### Final Question

Purpose:

- Convert model results into final decision, design rule, recommendation, classification rule, policy, or implementation plan.
- Explain tradeoffs and limits.

Common modeling choices:

- Multi-objective tradeoff table.
- Recommendation tiers and threshold rules.
- Pareto frontier, sensitivity-informed policy, robust plan.
- Operational workflow or reusable algorithm.
- Generalization conditions and failure boundaries.

Why strong teams choose this:

- It closes the loop from math to contest deliverable.
- It tells judges what to do with the result.

Reject the final route if:

- It only repeats previous numerical results.
- It gives recommendations not traceable to model outputs.
- It hides uncertainty or limitations.

### Fifth Or Extra Question

Purpose:

- Usually communication, generalization, extra scenario, implementation, or policy memo.
- Do not treat it as an unrelated essay.

Common modeling choices:

- Generalized algorithm, user-facing plan, memo, scenario extension, sensitivity summary.

Strong handling:

- Reuse earlier variables and results.
- State the model's scope and transfer conditions.
- Include one compact figure/table that supports the final message.

## Archetype Model-Choice Recipes

### Mechanism And Engineering

Think first:

- What physical quantity is conserved?
- What units must balance?
- Which parameters are measurable, bounded, or calibrated?

Model tournament:

- Baseline: dimensional analysis or simplified equation.
- Candidate 1: ODE/PDE/mechanism equation.
- Candidate 2: empirical fitting.
- Strong route: mechanism equation plus calibration or residual correction.

Validation:

- Unit check, limiting case, convergence, residuals, parameter sensitivity.

Choose this topic only if:

- The team can bound parameters and explain physical plausibility.

### Optimization And Scheduling

Think first:

- What are the decision variables?
- What is feasible before optimal?
- Which constraints are hard and which are soft?

Model tournament:

- Baseline: greedy, current policy, LP relaxation, shortest path.
- Candidate 1: MILP/network flow/dynamic programming.
- Candidate 2: heuristic/metaheuristic.
- Strong route: exact small cases plus scalable heuristic or robust optimization.

Validation:

- Constraint satisfaction, exact-small-case gap, runtime, scenario stress.

Choose this topic only if:

- A feasible plan can be produced early and the objective is not vague.

### Forecasting And Time Series

Think first:

- What decision uses the forecast?
- What horizon matters?
- Is there trend, seasonality, shock, or external covariate structure?

Model tournament:

- Baseline: naive, seasonal naive, moving average.
- Candidate 1: ARIMA/state-space/exponential smoothing.
- Candidate 2: ML with domain features.
- Strong route: simple baseline plus covariate/mechanism features and uncertainty intervals.

Validation:

- Rolling-origin validation, residual diagnostics, interval coverage, decision regret.

Choose this topic only if:

- Forecast errors can be converted into decision risk.

### Evaluation And Ranking

Think first:

- What alternatives are being compared?
- What indicators are valid, directional, non-duplicative, and observable?
- Does the final decision need ranking, grouping, thresholding, or diagnosis?

Model tournament:

- Baseline: equal weight, dominance/Pareto, normalized score.
- Candidate 1: entropy/AHP/TOPSIS/fuzzy.
- Candidate 2: PCA/factor analysis or clustering before ranking.
- Strong route: indicator mechanism plus rank stability and method comparison.

Validation:

- Weight perturbation, rank correlation, indicator ablation, known-case check.

Choose this topic only if:

- Indicator construction is problem-specific and rankings can be stress-tested.

### Data Mining, Classification, And Clustering

Think first:

- What is the target or decision object?
- Are labels reliable?
- Does the data have special constraints such as missingness, imbalance, closure, spatial/temporal dependence, or measurement drift?

Model tournament:

- Baseline: descriptive statistics, rule-based classifier, logistic regression, simple clustering.
- Candidate 1: tree/SVM/random forest/boosting.
- Candidate 2: transformation-aware or domain-feature model.
- Strong route: domain features plus baseline/ablation/cross-validation.

Validation:

- Confusion matrix, bootstrap stability, feature ablation, error cases, downstream decision effect.

Choose this topic only if:

- The team can build features beyond generic preprocessing.

### Network, Simulation, And Complex Systems

Think first:

- What are the states, actors, nodes, edges, flows, or transition rules?
- What intervention or policy is being tested?

Model tournament:

- Baseline: simple network metrics, deterministic scenario, small simulation.
- Candidate 1: weighted graph, Markov chain, queue, agent-based simulation.
- Candidate 2: game/equilibrium or Monte Carlo scenario generator.
- Strong route: calibrated rules plus intervention comparison and stress test.

Validation:

- Reproduce simple cases, compare with baseline metrics, sensitivity to rules, scenario stability.

Choose this topic only if:

- Rules are defensible and results produce a decision, not only animation-like behavior.

### Geometry, Localization, And Spatial Design

Think first:

- Is the solution identifiable?
- Are there mirror solutions or ill-conditioned geometries?
- What measurements produce error propagation?

Model tournament:

- Baseline: analytic geometry, triangulation, least squares.
- Candidate 1: nonlinear least squares.
- Candidate 2: robust estimation plus geometry-quality metric.
- Strong route: identifiability proof, residual analysis, and Monte Carlo error band.

Validation:

- Known-point reverse check, residuals, conditioning/GDOP, confidence ellipse.

Choose this topic only if:

- Uniqueness and error sensitivity can be explained.

## How To Use This Library During Selection

For each A/B/C candidate, write one line:

`Problem -> role chain -> baseline -> rejected alternatives -> chosen upgrade -> solver -> validation -> figure -> flip condition`

Then ask:

1. Which archetype gives the clearest baseline?
2. Which candidate has a main model that directly changes the final decision?
3. Which candidate has the strongest validation that can be produced within contest time?
4. Which candidate has a fallback that still yields a complete paper?
5. Which candidate has a non-generic visible figure/table?

Choose the topic whose complete chain survives, not the topic with the most impressive model names.

## Sources To Ground Claims

- CUMCM official site: https://www.mcm.edu.cn/
- CUMCM historical problem archive: https://www.mcm.edu.cn/html_cn/node/a53a84ead7b2e5087dc59954d440219a.html
- COMAP MCM/ICM contest matrix: https://www.contest.comap.com/undergraduate/contests/matrix/index.html
- COMAP previous contests page: https://www.contest.comap.com/undergraduate/contests/mcm/previous-contests.php
