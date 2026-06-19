---
name: math-modeling-contest-route-selection
description: Select superior mathematical modeling contest problems and modeling-solution routes for CUMCM A/B/C, MCM, ICM, and similar contests. Use when comparing contest topics, choosing modeling methods, distilling award-paper per-subquestion modeling/solving logic, auditing AI-generated topic choices, evaluating engineering feasibility, designing baseline-main-validation-refutation model stacks, or proving why one problem/method route is more executable and paper-worthy than alternatives.
---

# Math Modeling Contest Route Selection

## Overview

Use this skill to prevent blind AI topic choice. The central object is not just "which problem should we choose"; it is "which problem has the strongest feasible modeling route under contest time, data, coding, validation, and paper-writing constraints."

For CUMCM, always compare A/B/C through two layers:

1. Problem selection: Does this topic have enough clarity, data/parameter access, and paper narrative?
2. Method-route selection: Can the team implement, solve, validate, and explain a superior modeling path?

Choose the problem whose best method route is strongest. Do not choose a problem merely because its domain looks familiar or its generic AI plan sounds impressive.

## CUMCM A/B/C Workflow

1. Parse all three problems before recommending any one.
   - Extract task outputs, inferred judge-visible criteria, data/parameter needs, constraints, likely figures/tables, and final decision objects.
   - If only letters A/B/C are provided, ask for the full statements or give only a provisional prior.

2. Build one "problem card" for each problem.
   - Domain: engineering/physics, optimization, data analysis, public policy, evaluation, forecasting, network, simulation, or hybrid.
   - Mathematical core: mechanism model, optimization, prediction, evaluation, simulation, uncertainty, graph/network, control, or data mining.
   - Deliverables: what the paper must calculate, rank, predict, optimize, explain, or recommend.
   - Risks: missing data, fragile assumptions, excessive coding, weak validation, unclear outputs, or generic method stack.
   - Crowding risk: whether many teams will use the same obvious method stack; if high, include `crowd_escape_mechanism`.
   - Team fit: whether the route matches the team's coding, domain, optimization, statistics, or physics strengths.

3. Build at least two "method route cards" for each plausible problem.
   - Minimum viable route: simplest route that can finish a coherent paper.
   - Strong paper route: route with the best originality/validation/presentation balance.
   - Optional ambitious route: only include if failure can fall back to the minimum route.
   - When sub-questions are available, map them to role-based slots (`first`, `main`, `extend`, `final`) instead of assuming every problem has exactly Q1-Q4.
   - For any fully stated problem, `question_chain` is mandatory. Do not finalize a recommendation if a route card has no sub-question chain; mark the chain as provisional only when the statement itself is unavailable.
   - For each sub-question, explain why the chosen model was selected over at least one simpler or fashionable alternative.

4. Compare method routes before comparing final topics.
   - A weaker topic with a robust, elegant route can beat an attractive topic whose route is vague.
   - A fashionable method does not help unless it improves a measurable output, supports validation, or creates a clearer paper story.
   - Show topic differentiation and best-route differentiation separately when they disagree.
   - Run a model-choice tournament: baseline, one rejected alternative, chosen route, deciding test, and flip condition.

5. Recommend one primary problem and one fallback.
   - The fallback should reuse part of the team's prepared code, data workflow, or method stack where possible.
   - If the top two final scores differ by 0.20 or less on a 0-5 scale, state that the lead is uncertain; if they differ by 0.05 or less, call it a near tie.
   - Include the strongest reason to reject the primary problem and the test or evidence that lets it survive.

## Method Route Card

For every candidate route, fill these fields:

- `core_question`: What mathematical question does this route answer?
- `decision_variables_or_states`: Variables, states, indicators, or predicted objects.
- `assumptions`: Necessary assumptions and how to stress-test them.
- `binding_constraints`: Hard constraints that can make the route infeasible, such as actuator stroke, adjacent-node deformation, capacity, inventory, conservation, boundary, time, or budget limits.
- `baseline`: Simple model that must be beaten or extended.
- `main_model`: Main equations/algorithm/model family.
- `solver_or_algorithm`: How it will be computed within contest time.
- `data_or_parameters`: Source, estimation method, or defensible synthetic plan.
- `validation`: Baseline comparison, sensitivity, ablation, external consistency, limiting case, or simulation stress test.
- `model_choice_rationale`: Why this model family fits the deliverable better than alternatives.
- `rejected_alternatives`: Simpler or fashionable methods considered and why they are weaker.
- `refutation_tests`: Tests that could disprove this route.
- `paper_figures`: Figures/tables that make the route visible to judges.
- `fallback`: Include `trigger`, `action`, and preferably `deadline`. Example: "If clustering silhouette stays below 0.25 after standardization and log-ratio transforms by Day 2 noon, switch to hierarchical clustering plus interpretable decision tree."
- `question_chain`: For each sub-question, role, deliverable, baseline, main model or upgrade, model-choice rationale, rejected alternative, refutation test, solver, validation, figure/table, fallback, and how it supports the next question.
- `superiority_claim`: One sentence explaining why this route is better than the generic AI route.

When using `scripts/score_topics.py`, `notes.highlight` is shown first in the route highlight column; `superiority_claim` is used as the fallback highlight.
For scoring JSON, add `evidence` and `flip_condition` at topic and route level. Use objects keyed by score criterion for decisive high or low scores; a single overall string is not enough to justify every decisive criterion. Use structured fallback objects when possible:
`{"trigger": "...", "action": "...", "deadline": "..."}`.
For `question_chain`, either provide explicit `question_weight` for every sub-question or omit all sub-question weights and let the script use role-based defaults.
For popular or crowded topics, add `crowd_escape_mechanism` at topic or route level. For team-dependent decisions, add `team_profile`, `team_fit_blend`, and each topic's `team_fit_score` or `team_fit: {"score": ..., "rationale": ...}`.

## Engineering Feasibility Gate

Reject or downgrade a route if any answer is missing:

- Can the model be implemented with the team's actual coding ability?
- Are the input variables measurable or defensibly estimated?
- Is there a baseline result within the first contest day?
- Can the main solver finish fast enough for iteration?
- Can errors, parameters, or weights be stress-tested?
- Can the final results become clear plots/tables rather than only prose?
- Is there a fallback route if data collection, tuning, or optimization fails?

Read `references/engineering-feasibility.md` when judging implementation load, solver risk, and fallback design.

## Anti-Homogeneity Rules

Treat a plan as too generic if it contains any of these patterns:

- "Use entropy weight/TOPSIS/AHP/grey prediction/LSTM/random forest" without problem-specific feature construction or validation.
- A method list that could fit any contest problem after replacing nouns.
- No baseline model.
- No reason why the chosen model beats at least one simpler or common alternative.
- No refutation test that could disprove the chosen route.
- High topic differentiation score on a crowded topic without a `crowd_escape_mechanism`.
- Strong route differentiation on a crowded or only moderately differentiated topic without a named `crowd_escape_mechanism`.
- No route-level fallback.
- Fallback has no measurable trigger, deadline, or switch condition.
- No failure mode analysis.
- No inventory of binding constraints for constrained optimization, physics, engineering, supply-chain, or capacity-planning routes.
- No explanation of why a simpler model is insufficient.
- No quantitative validation route.
- A paper highlight that only says "comprehensive," "accurate," "innovative," or "multi-factor."

When a plan fails this check, rewrite it by forcing:

- One domain-specific metric or state variable.
- One baseline comparison.
- One robustness, sensitivity, or ablation experiment.
- One binding-constraint inventory, with the constraints that are most likely to break feasibility.
- One solver or coding plan.
- One judge-visible visualization.
- One fallback model with a trigger condition and action that can still produce a full paper.

## Resource Routing

- Read `references/contest-archives.md` when the user asks for historical grounding, official archive links, or long-horizon contest pattern distillation.
- Read `references/award-method-distillation.md` when the user asks what national-award or excellent papers tend to do, or wants historical solution-method inspiration before choosing A/B/C.
- Read `references/award-question-decomposition.md` when the user asks how each sub-question should be reasoned, modeled, validated, or connected into a national-award-style paper.
- Read `references/award-route-pattern-library.md` when the user asks to distill how award-style papers model and solve problem 1, problem 2, problem 3, and later sub-questions.
- Read `references/refutation-and-model-choice.md` when auditing or improving topic choice, model choice, rejected alternatives, flip conditions, or self-refutation loops.
- Read `references/paper-scoring-framework.md` when the user asks for scoring standards, paper competitiveness, multi-dimensional evaluation, or judge-visible strengths and weaknesses.
- Read `references/problem-taxonomy.md` when classifying A/B/C problem types or finding differentiated angles.
- Read `references/method-map.md` when mapping problem symptoms to modeling method families.
- Read `references/engineering-feasibility.md` when auditing solver complexity, data pipelines, fallback routes, and implementation realism.
- Read `references/selection-rubric.md` when scoring A/B/C or auditing final recommendations.
- Run `scripts/score_topics.py <input.json>` for final A/B/C ranking whenever possible; do not hand-reconstruct the final table if a scoring JSON can be written. Use `--help` to see CLI options.

## Output Format

Use a compact output for quick topic selection, and a deep output when the user asks for per-question planning, paper design, scoring standards, or national-award-style reasoning.

For CUMCM A/B/C selection, return:

1. `Conclusion`: primary problem, fallback problem, and one-sentence reason.
2. `Score-gap note`: state near tie (<=0.05), moderate uncertainty (>0.05 and <=0.20), or evidence-backed separation (>0.20).
3. `A/B/C comparison`: topic score, best route score, topic differentiation, route differentiation, main risk, feasibility judgment, and decisive evidence/flip condition.
4. `Crowding and team-fit note`: obvious generic route, crowd-escape mechanism, and whether team strengths could flip the recommendation.
5. `Route comparison`: minimum viable route, strong paper route, optional ambitious route; include route-level evidence and flip condition for decisive scores.
6. `Model-choice tournament`: baseline, rejected alternative, chosen route, deciding test, and flip condition.
7. `Question-chain sketch`: one line per sub-question role (`first`, `main`, `extend`, `final`) naming deliverable, baseline, chosen model, rejected alternative, why chosen, refutation test, validation, figure, fallback trigger/action, and dependency.
8. `Refutation ledger`: strongest reason to choose, strongest reason to reject, test that decides, flip condition, and rescue.
9. `Recommended modeling stack`: baseline, main model, solver, validation, sensitivity, fallback trigger/action.
10. `Why this is superior`: why this route beats the generic AI plan and the other two problems.
11. `Engineering plan`: data, code modules, solver steps, figures, and timeline.
12. `Risks and rescue`: what to do if data/model/solver/time fails; every rescue must have a measurable trigger or deadline.

For a single chosen problem, return:

1. Problem DNA.
2. Generic AI route to avoid.
3. Minimum viable route.
4. Strong paper route.
5. Model-choice tournament: baseline, rejected alternatives, chosen route, deciding test, and flip condition.
6. Role-based sub-question chain: required deliverable, baseline, chosen model/upgrade, rejected alternative, why chosen, refutation test, solver, validation, figure/table, fallback trigger/action, and dependency.
7. Route-level scoring.
8. Validation, ablation, refutation, and sensitivity plan.
9. Paper narrative and figure plan.

For deep paper planning, add:

1. Pre-selection score: feasibility, data/parameter access, day-one baseline, validation opportunity, and differentiation opportunity.
2. Paper-competitiveness score: deliverable alignment, assumption quality, model fit/originality, reproducibility, validation, decision value, expression, engineering feasibility, and differentiation.
3. Score-gap note: if candidates differ by 0.05 or less on a 0-5 scale, treat them as a near tie and choose by team strengths.
4. Moderate-uncertainty note: if candidates differ by more than 0.05 but no more than 0.20, state that the lead is not decisive unless decisive criteria have written evidence.
