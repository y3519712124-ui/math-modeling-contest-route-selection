# Method Map

Use this file to map problem symptoms to modeling methods. Always pair methods with baseline, solver plan, validation, and paper expression.

## Selection Principle

Choose the smallest method stack that can answer the decision question and survive contest engineering constraints. A strong contest paper often uses:

- Baseline model: simple, explainable, hard to beat.
- Main model: adds the core insight.
- Solver plan: deterministic enough to finish and iterate.
- Validation model: checks robustness, sensitivity, ablation, or external consistency.

Do not select a method because it is advanced. Select it because it changes a decision, improves a baseline, handles a known weakness, or makes the paper more defensible.

## Method Families

| Problem symptom | Baseline | Strong route | Solver plan | Validation |
| --- | --- | --- | --- | --- |
| allocate scarce resources | greedy allocation, LP relaxation | integer programming, robust optimization, multi-objective optimization | scipy/pulp/ortools; exact on small cases, heuristic on large cases | constraint satisfaction, Pareto analysis, sensitivity |
| route or schedule items | nearest-neighbor, shortest path, assignment | MILP, dynamic programming, tabu/genetic/simulated annealing | start with deterministic heuristic, then improve; log convergence | compare with greedy/exact small cases |
| forecast values | naive, moving average, exponential smoothing | ARIMA/state-space, gradient boosting, hybrid mechanism features | rolling training window; keep feature pipeline simple | rolling validation, residual diagnostics, decision regret |
| rank/evaluate alternatives | normalized indicators, dominance, PCA | entropy/AHP/TOPSIS/fuzzy only if indicators are justified | spreadsheet/Python table pipeline with rank-stability loop | weight perturbation, rank stability, known-case check |
| simulate physical process | dimensional analysis, simplified ODE | mechanism equations, finite difference, parameter calibration | solve simple case analytically before numerical simulation | limiting cases, convergence, physical sanity |
| model spread or diffusion | logistic/SIR/SIS | network epidemic, Markov chain, agent-based simulation | calibrate few parameters; avoid huge arbitrary simulations | reproduce known curves, parameter sensitivity |
| classify or extract patterns | rules, thresholding, classical features | random forest/SVM/CNN only when data supports it | cross-validation pipeline; save confusion matrix and errors | confusion matrix, ablation, downstream error |
| analyze compositional or percentage-sum data | raw percentage summaries, boxplots, simple tests | log-ratio transform (CLR/ILR) + closed-sum-aware clustering/discriminant + correction model | check zeros/missing values, transform, then model; keep raw baseline for comparison | sub-composition stability, corrected vs uncorrected ablation, known-class recovery |
| bearing-only or passive localization | analytic triangulation from known transmitters | identifiability/minimum-source proof + condition number/GDOP + error propagation + robust adjustment | solve closed-form cases first, then least-squares/robust optimization with residual checks | reverse-check known positions, Monte Carlo deviation bands, geometric residuals |
| understand policy effect | descriptive statistics, regression | causal graph, scenario simulation, synthetic control | keep assumptions explicit; test placebo or counterfactual cases | placebo tests, sensitivity to assumptions |
| handle uncertainty | deterministic point estimate | Monte Carlo, stochastic programming, Bayesian interval | separate sampling code from model code; report intervals | confidence intervals, scenario stress test |
| manage strategic behavior | payoff matrix, simple equilibrium | evolutionary game, agent simulation | start with 2-3 actor types; calibrate behavior rules | equilibrium plausibility, behavioral sensitivity |

## Combinations That Often Work

- Forecasting + optimization: predict demand, then optimize allocation; validate decision regret under forecast errors.
- Evaluation + clustering: cluster objects first, then apply different evaluation weights per group.
- Mechanism + machine learning: use physical or domain equations to create features, then fit a predictive model.
- Network + intervention: rank nodes/edges, then simulate removal, protection, or subsidy policies.
- Simulation + robust decision: simulate scenarios, then choose policy that is stable under worst plausible cases.

## CUMCM A/B/C Method Priors

Use these only as priors. The actual statement overrides them.

- A-type problems often reward mechanism modeling, engineering physics, simulation, dimensional analysis, and parameter sensitivity. A strong A route usually needs equations, physical sanity checks, and clear plots.
- B-type problems often reward optimization, operations research, network analysis, scheduling, resource allocation, or policy simulation. A strong B route usually needs decision variables, constraints, objective functions, and solver comparisons.
- C-type problems often reward data processing, evaluation, prediction, clustering, statistical modeling, and indicator systems. A strong C route usually needs data cleaning, feature construction, baseline comparison, and rank/prediction stability.

Do not choose C only because it looks "data-driven." Do not avoid A only because it has formulas. Choose the problem with the best executable route.

## Common Misuses

- AHP when no expert comparison matrix can be justified.
- Entropy weight when indicator variance is a data artifact rather than importance.
- Neural network on tiny data.
- Metaheuristic without a baseline or convergence evidence.
- Fuzzy evaluation used to hide unclear indicators.
- Regression treated as causal proof.
- Raw Euclidean clustering or PCA on percentage-sum composition data without checking closed-sum effects.
- Bearing-only localization without identifiability, mirror-symmetry, or error-propagation checks.
- Stacking three advanced methods when one baseline plus one justified upgrade would be clearer.
- Optimizing an objective that is not connected to the deliverable asked by the problem.

## Paper-Level Method Narrative

Write method choices as:

1. "The problem requires X, so the baseline is Y."
2. "The baseline fails under Z, so the upgraded model adds W."
3. "The solver is feasible because S."
4. "We validate the upgrade by V."
5. "The final result changes decision D, not just metric M."
