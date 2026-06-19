# Problem Taxonomy For Topic Selection

Use this taxonomy to classify candidate problems and find judge-visible differentiation angles.

## 1. Operations And Logistics

Typical signals: routing, scheduling, allocation, facility location, inventory, traffic, emergency dispatch.

Common generic route: build a mixed integer program, then use a heuristic.

Differentiation levers:

- Add uncertainty through robust or stochastic optimization.
- Build a two-stage model: feasibility first, then quality optimization.
- Compare exact, greedy, and metaheuristic baselines.
- Visualize bottlenecks and marginal value of constraints.

Risks:

- Too many variables for contest time.
- No interpretable reason why the final plan is better.
- Heuristic parameters selected without sensitivity analysis.

## 2. Forecasting And Time Series

Typical signals: demand, trend, population, climate, traffic flow, sales, disease counts.

Common generic route: ARIMA, grey model, LSTM, or random forest without error analysis.

Differentiation levers:

- Separate trend, seasonality, shock, and policy variables.
- Use rolling-origin validation.
- Compare simple baselines before complex models.
- Convert predictions into decisions and quantify decision regret.

Risks:

- Overfitting short data.
- Reporting prediction accuracy without showing impact on the contest decision.

## 3. Evaluation And Ranking

Typical signals: quality index, performance evaluation, resource priority, comprehensive score.

Common generic route: AHP/entropy weight/TOPSIS with arbitrary indicators.

Differentiation levers:

- Derive indicators from problem mechanism, not only availability.
- Run weight perturbation and rank stability analysis.
- Use Pareto fronts or dominance relations before collapsing to one score.
- Explain what each indicator changes in the final decision.

Risks:

- Indicator soup.
- Scores that cannot be validated against outcomes or expert logic.

## 4. Public Policy And Social Systems

Typical signals: health, education, aging, disaster response, city governance, equity, behavior.

Common generic route: collect factors, regress outcome, make broad recommendations.

Differentiation levers:

- Model stakeholder objectives separately.
- Include fairness, cost, and feasibility constraints.
- Use scenario simulation to compare policies.
- Make assumptions auditable and ethically explicit.

Risks:

- Vague recommendations.
- Lack of measurable policy outputs.

## 5. Environment, Resources, And Sustainability

Typical signals: carbon, water, energy, agriculture, ecology, waste, climate.

Common generic route: multi-index evaluation plus prediction.

Differentiation levers:

- Couple physical balance equations with data-driven estimates.
- Quantify uncertainty in environmental parameters.
- Evaluate tradeoffs among ecological, economic, and social objectives.
- Use spatial or temporal heterogeneity rather than global averages.

Risks:

- Big assumptions with no sensitivity test.
- Good-looking indices that do not support concrete intervention.

## 6. Engineering Physics And Mechanism Models

Typical signals: motion, heat, fluid, optics, materials, structures, control.

Common generic route: write equations and simulate one case.

Differentiation levers:

- Non-dimensionalize variables to reduce parameter burden.
- Validate limiting cases analytically.
- Compare simplified closed-form model and numerical simulation.
- Show parameter sensitivity and physical plausibility.

Risks:

- Equations detached from required deliverables.
- Numerical results without convergence or sanity checks.

## 7. Graphs, Networks, And Complex Systems

Typical signals: spread, connectivity, influence, transport network, supply chain, communication.

Common generic route: centrality metrics or SIR model only.

Differentiation levers:

- Use multilayer or weighted networks when the problem implies heterogeneous links.
- Compare topology-only metrics with flow-aware metrics.
- Simulate targeted failures or interventions.
- Make node/edge definitions problem-specific.

Risks:

- Network built because it looks modern, not because relationships matter.

## 8. Image, Signal, And Data Mining

Typical signals: classification, recognition, extraction, sensor data, image measurement.

Common generic route: use a neural network and report accuracy.

Differentiation levers:

- Design preprocessing and domain-specific features.
- Use interpretable measurements when data is small.
- Include error propagation from recognition to final decision.
- Compare classical and learning-based pipelines.

Risks:

- Training data too small.
- No link between algorithm accuracy and modeling objective.

## 9. Compositional, Chemical, And Percentage-Sum Data

Typical signals: chemical composition, oxide percentages, ingredient proportions, element ratios, components that sum to a fixed total.

Common generic route: run raw-percentage PCA, K-means, Fisher discriminant, or random forest directly.

Differentiation levers:

- Treat the data as compositional: raw percentages have closed-sum constraints and Euclidean distances can mislead.
- Use log-ratio transforms such as CLR or ILR after handling zeros/missing values.
- Compare raw-percentage baseline against log-ratio-aware clustering or classification.
- For weathering/corrosion problems, build a correction or recovery model and ablate corrected versus uncorrected features.
- Report interpretable component ratios and class rules, not only classifier accuracy.

Risks:

- Small sample size and class imbalance.
- Overclaiming chemical mechanism from weak statistical evidence.
- Transformation choices can become black boxes if not explained.

## 10. Bearing-Only Localization And Geometric Identifiability

Typical signals: pure bearing, passive localization, direction-of-arrival angles, transmitter/receiver geometry, formation adjustment, minimum sensors.

Common generic route: triangulate with sine/cosine law, then run a least-squares adjustment.

Differentiation levers:

- Prove identifiability and handle mirror-symmetry ambiguity before optimization.
- Analyze the minimum number and geometry of transmitters/sources.
- Use condition number, GDOP, Jacobian error propagation, or confidence ellipses to explain when localization is stable.
- Validate by reverse-checking known positions and Monte Carlo angle-noise perturbations.
- Compare robust adjustment against greedy one-step adjustment or naive least squares.

Risks:

- Multiple geometric solutions can satisfy the same bearing constraints.
- Good-looking simulation may hide unobservable configurations.
- Adjustment strategies can be arbitrary without residual and convergence checks.

## 11. Simulation, Games, And Agent Behavior

Typical signals: crowd behavior, competition, strategy, evacuation, market choice, repeated interaction.

Common generic route: agent simulation with arbitrary rules.

Differentiation levers:

- Calibrate behavior rules from observable constraints.
- Compare equilibrium, heuristic, and simulation outcomes.
- Use sensitivity analysis on behavior parameters.
- Report emergent patterns, not only animations.

Risks:

- Rules feel invented.
- No validation against known limiting cases or real observations.
