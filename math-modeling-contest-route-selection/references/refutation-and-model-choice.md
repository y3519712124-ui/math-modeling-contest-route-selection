# Refutation And Model-Choice Workflow

Use this file when an AI-generated topic choice or modeling route looks plausible but may be generic, overconfident, or under-validated.

## Core Principle

A superior modeling route is the one that survives structured refutation. Do not ask only "Which model can solve this?" Ask:

1. What claim does this model make?
2. What simpler model could also answer the question?
3. What evidence would make the simpler model insufficient?
4. What condition would make the chosen model fail?
5. What fallback still produces a complete paper?

## The Two-Level Refutation Loop

### Level 1: Topic Refutation

Apply before choosing A/B/C.

Refute these claims for each topic:

- Feasibility claim: the team can finish models, code, figures, and paper.
- Data claim: required data or parameters are available or defensibly estimated.
- Differentiation claim: the route will not look like a generic AI answer.
- Validation claim: the result can be checked quantitatively.
- Narrative claim: the paper can tell a clear story from variables to decision.
- Rescue claim: failure still leaves a complete paper.

Reject or downgrade a topic if:

- The first-day baseline is unclear.
- The main model cannot be validated.
- The best route depends on guessed parameters without sensitivity.
- The fallback is only a weaker method name, not a trigger-action plan.
- The final answer is prose rather than a measurable decision.

### Level 2: Method-Route Refutation

Apply after selecting each candidate route.

For every route, create a model-choice tournament:

| Candidate | What it answers | Why it might be enough | Why it may fail | Test that decides | Outcome |
| --- | --- | --- | --- | --- | --- |
| Baseline | Minimal deliverable | Fast and interpretable | Misses key mechanism/constraint | Baseline error or decision loss | keep as benchmark |
| Alternative 1 | Simpler upgrade | Easier to implement | May ignore uncertainty/nonlinearity | ablation or residual test | accept/reject |
| Alternative 2 | Different model family | Captures another structure | Higher complexity | small-case or CV test | accept/reject |
| Chosen route | Final paper route | Directly fixes baseline weakness | Solver/data risk | validation + stress test | primary/fallback |

Do not choose a route until the chosen model has beaten at least one baseline or alternative by a named test.

## Required Refutation Fields

Every strong route should include:

- `model_choice_rationale`: why this model family fits the problem deliverable.
- `rejected_alternatives`: simpler or fashionable methods considered and why they are weaker.
- `refutation_tests`: tests that could disprove the route, such as residual failure, unstable rankings, poor cross-validation, non-convergence, infeasible constraints, or sensitivity reversal.
- `flip_condition`: what would make another topic or route become preferable.
- `fallback`: structured as `trigger`, `action`, and preferably `deadline`.

Every strong sub-question chain should include:

- deliverable
- baseline
- chosen model or upgrade
- why this model
- solver
- validation
- fallback trigger/action
- dependency into the next sub-question

## Refutation Tests By Model Family

### Mechanism Models

Disprove with:

- unit mismatch
- wrong limiting case
- parameter sensitivity reverses the conclusion
- residuals show systematic structure
- calibrated parameters are physically implausible

Repair:

- simplify equations
- add bounded correction term
- calibrate only identifiable parameters
- report uncertainty band

### Optimization Models

Disprove with:

- infeasible constraints
- objective not aligned with deliverable
- exact small cases beat the heuristic
- runtime prevents iteration
- scenario stress changes the recommended plan

Repair:

- relax constraints
- use greedy/local-search fallback
- split objective into primary and secondary goals
- report optimality gap or regret

### Forecasting Models

Disprove with:

- naive or seasonal baseline performs similarly
- rolling validation fails
- residual autocorrelation remains
- forecast error does not affect final decision
- scenario shocks dominate model differences

Repair:

- use simpler baseline plus intervals
- add domain covariates
- evaluate decision regret instead of only prediction error

### Evaluation And Ranking Models

Disprove with:

- rankings reverse under small weight perturbations
- indicators duplicate the same information
- normalization changes the conclusion
- known cases are ranked implausibly

Repair:

- use Pareto/dominance baseline
- cluster before ranking
- report stable tiers instead of exact ranks
- remove redundant indicators

### Machine Learning Models

Disprove with:

- leakage, imbalance, overfitting
- weak baseline gap
- unstable feature importance
- high accuracy but wrong downstream decision
- no interpretability for final recommendation

Repair:

- use interpretable baseline
- add domain features
- run ablation
- propagate prediction error into the final decision

### Simulation And Agent Models

Disprove with:

- rules are uncalibrated
- small deterministic cases do not match expectations
- results depend on arbitrary random seeds
- policy ranking reverses under plausible behavior parameters

Repair:

- reduce actor types
- calibrate rules from available data or constraints
- report scenario bands
- use robust recommendation instead of single optimum

## Flip Conditions

A flip condition must be measurable. Avoid "if results are bad." Use:

- "If the Day 1 baseline cannot produce the required deliverable by 18:00, switch topics."
- "If MILP solve time exceeds 10 minutes for the full instance, switch to greedy plus local search."
- "If rank Kendall tau drops below 0.7 under weight perturbation, report tiers or choose another route."
- "If Monte Carlo error bands overlap all design alternatives, prefer the simpler robust plan."
- "If cross-validation improvement over logistic regression is below 3 percentage points, use the interpretable baseline."

## The Perfecting Loop

Run this loop after the first route design:

1. State the current top topic and route.
2. Write the strongest argument against choosing it.
3. Try to replace it with the simplest viable model.
4. Identify the one test that decides between simple and advanced.
5. Add the test to the plan and score JSON.
6. If the route survives, strengthen the paper narrative.
7. If it fails, downgrade the route or choose the fallback.

Repeat until the remaining route has:

- a day-one baseline
- a justified main upgrade
- an implementable solver
- at least one validation or ablation
- a structured fallback
- a written flip condition
- a judge-visible figure or table

## Output Shape

For A/B/C selection, include a compact refutation ledger:

| Topic | Strongest reason to choose | Strongest reason to reject | Test that decides | Flip condition | Rescue |
| --- | --- | --- | --- | --- | --- |

For the chosen route, include:

| Sub-question | Baseline | Chosen model | Rejected alternative | Why chosen | Validation | Failure trigger | Rescue action |
| --- | --- | --- | --- | --- | --- | --- | --- |

If no route survives this ledger, do not force a primary recommendation. Say the choice is provisional and specify what information is needed.
