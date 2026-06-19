# Engineering Feasibility For Modeling Routes

Use this file to audit whether a CUMCM A/B/C modeling method can actually be implemented, solved, validated, and written during the contest.

## Feasibility Dimensions

Score every route from 0 to 5 on:

- Problem fit: The method directly answers the asked output.
- Engineering solvability: The team can code, debug, and run it repeatedly.
- Data/parameter control: Inputs are available, estimable, or defensibly assumed.
- Solver stability: The algorithm is not too slow, random, or parameter-sensitive.
- Validation strength: Baseline, sensitivity, ablation, or external check is possible.
- Paper explainability: Equations, algorithm steps, and results can be explained clearly.
- Figure/table potential: The route naturally produces judge-visible evidence.
- Fallback robustness: A simpler route can still produce a complete paper.

## Day-One Baseline Rule

A route is unsafe if it cannot produce a baseline result on day one.

Day-one baseline examples:

- Optimization: greedy or relaxed LP solution.
- Forecasting: naive or exponential smoothing forecast.
- Evaluation: normalized indicator table and preliminary ranking.
- Mechanism model: simplified equation or limiting-case simulation.
- Network: basic centrality or shortest-path result.
- Image/data mining: rule-based extraction or classical feature baseline.

## Solver Risk Levels

Low risk:

- Closed-form calculation, linear regression, simple ODE, PCA, TOPSIS with justified indicators, greedy heuristic, small LP/MILP.

Medium risk:

- Nonlinear optimization, medium MILP, Monte Carlo, random forest, SVM, finite difference simulation, network intervention simulation.

High risk:

- Deep learning from scratch, large MILP without decomposition, complex agent-based simulation, multi-objective metaheuristic with many parameters, causal inference without credible assumptions.

High-risk routes must include a fallback and an ablation plan.

Any route that depends on a high-risk or fashionable model must also name:

- The simpler baseline it must beat.
- The rejected alternative that would be used if the main model fails.
- The deciding test, such as runtime, residual error, rank stability, validation score, optimality gap, or sensitivity reversal.
- The flip condition that makes the safer route preferable.

## Route Rescue Patterns

- If data collection fails: switch to parameter ranges and scenario simulation.
- If optimization is too slow: solve small exact cases, then use heuristic for full scale.
- If neural model underperforms: use feature-based classical model and error analysis.
- If weights are controversial: report rank stability under weight perturbation.
- If mechanism parameters are uncertain: report sensitivity bands and limiting cases.
- If simulation rules feel arbitrary: reduce agent types and justify rules from observed constraints.

Every rescue route needs a trigger condition and action, not only a vague fallback sentence.

Use this form:

- Trigger: measurable condition, deadline, residual threshold, solver runtime, instability metric, or validation failure.
- Action: simpler model or safer output that can still produce a complete paper.
- Deadline: when to stop trying the strong route.

Examples:

- If the solver cannot produce a feasible solution by the end of Day 1, switch to the deterministic baseline.
- If a heuristic changes the selected policy under small random seeds or parameter perturbations, report it as exploratory and submit the baseline route.
- If a high-fidelity model needs more inputs than the problem provides, bound those inputs and submit sensitivity bands.
- If a generalized recursion cannot be written by Day 2, solve the small case rigorously and present the general method as modular pseudocode.
- If clustering silhouette remains below 0.25 across three preprocessing variants by Day 2 noon, switch to hierarchical clustering plus interpretable rules.
- If a localization residual exceeds 1 degree or Monte Carlo median position error exceeds the formation tolerance, switch to robust least squares and report confidence ellipses.

## Engineering Output Checklist

Before recommending a route, name:

- Code modules to write.
- Required data tables.
- Solver or package.
- Runtime expectation.
- Baseline result.
- Main experiment.
- Sensitivity or ablation experiment.
- Model-choice/refutation test.
- Key figure/table.
- Fallback submission path.
