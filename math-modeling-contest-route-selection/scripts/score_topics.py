#!/usr/bin/env python3
"""Score contest topics and their modeling-method routes from JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_TOPIC_CRITERIA = [
    {
        "key": "feasibility",
        "label": "Feasibility",
        "weight": 0.18,
        "description": "Can the team finish models, code, figures, and paper in time?",
    },
    {
        "key": "data_or_parameter_access",
        "label": "Data/Parameters",
        "weight": 0.14,
        "description": "Are data, parameters, or defensible assumptions available?",
    },
    {
        "key": "differentiation",
        "label": "Topic Differentiation",
        "weight": 0.18,
        "description": "Can the topic avoid generic AI similarity and show a clear angle?",
    },
    {
        "key": "validation_strength",
        "label": "Validation",
        "weight": 0.16,
        "description": "Can results be tested, compared, or stress-checked?",
    },
    {
        "key": "method_fit",
        "label": "Method Fit",
        "weight": 0.12,
        "description": "Do natural methods answer the problem rather than decorate it?",
    },
    {
        "key": "narrative_power",
        "label": "Narrative",
        "weight": 0.10,
        "description": "Can the paper tell a compact, convincing story?",
    },
    {
        "key": "risk_control",
        "label": "Risk Control",
        "weight": 0.12,
        "description": "Are fallback models and failure plans available?",
    },
]

DEFAULT_ROUTE_CRITERIA = [
    {
        "key": "route_problem_fit",
        "label": "Route Fit",
        "weight": 0.16,
        "description": "Does the route directly answer the required output?",
    },
    {
        "key": "engineering_solvability",
        "label": "Engineering",
        "weight": 0.16,
        "description": "Can the team implement, debug, and run the route in contest time?",
    },
    {
        "key": "data_parameter_control",
        "label": "Input Control",
        "weight": 0.14,
        "description": "Are inputs available, estimable, or defensibly assumed?",
    },
    {
        "key": "validation_design",
        "label": "Route Validation",
        "weight": 0.14,
        "description": "Is there a concrete baseline, sensitivity, ablation, or external check?",
    },
    {
        "key": "route_differentiation",
        "label": "Route Differentiation",
        "weight": 0.14,
        "description": "Does the route avoid generic AI method stacking?",
    },
    {
        "key": "paper_explainability",
        "label": "Explainability",
        "weight": 0.10,
        "description": "Can the route be explained with clear equations, steps, and figures?",
    },
    {
        "key": "implementation_cost_control",
        "label": "Cost Control",
        "weight": 0.08,
        "description": "Is runtime and coding complexity controlled?",
    },
    {
        "key": "fallback_robustness",
        "label": "Fallback",
        "weight": 0.08,
        "description": "Can a simpler route still produce a complete paper?",
    },
]

DEFAULT_QUESTION_CRITERIA = [
    {
        "key": "role_alignment",
        "label": "Role Alignment",
        "weight": 0.18,
        "description": "Is the sub-question mapped to a useful role rather than a fixed Q1-Q4 template?",
    },
    {
        "key": "deliverable_clarity",
        "label": "Deliverable",
        "weight": 0.18,
        "description": "Does the sub-question have a measurable output, decision, ranking, prediction, or explanation target?",
    },
    {
        "key": "baseline_to_upgrade_logic",
        "label": "Baseline Upgrade",
        "weight": 0.22,
        "description": "Does the route move from a day-one baseline to one justified problem-specific upgrade?",
    },
    {
        "key": "dependency_structure",
        "label": "Dependency",
        "weight": 0.14,
        "description": "Does this answer feed the next sub-question or final conclusion?",
    },
    {
        "key": "validation_opportunity",
        "label": "Validation Opportunity",
        "weight": 0.16,
        "description": "Is there a plausible comparison, sensitivity, ablation, limiting case, or external check?",
    },
    {
        "key": "fallback_completeness",
        "label": "Fallback",
        "weight": 0.12,
        "description": "Can the paper stay complete if the main upgrade fails?",
    },
]

DEFAULT_BLEND = {"topic_weight": 0.45, "route_weight": 0.55}
DEFAULT_ROUTE_QUESTION_BLEND = {"route_weight": 0.70, "question_chain_weight": 0.30}
DEFAULT_TEAM_FIT_BLEND = {"model_score_weight": 0.85, "team_fit_weight": 0.15}
DECISIVE_HIGH_SCORE = 4.4
DECISIVE_LOW_SCORE = 3.5
GAP_BOUNDARY_BUFFER = 0.02
EVIDENCE_FIELDS = ("evidence", "decisive_evidence", "score_evidence")
FLIP_FIELDS = ("flip_condition", "flip_conditions", "decisive_flip_condition", "score_flip_condition")
TEAM_FIT_FIELDS = ("team_fit_score", "team_fit")
CROWD_ESCAPE_FIELDS = (
    "crowd_escape_mechanism",
    "anti_homogeneity_mechanism",
    "differentiation_evidence",
)
MODEL_CHOICE_FIELDS = ("model_choice_rationale", "why_this_model", "why_chosen", "choice_rationale")
REJECTED_ALTERNATIVE_FIELDS = (
    "rejected_alternatives",
    "rejected_alternative",
    "alternatives_rejected",
    "model_alternatives",
)
REFUTATION_FIELDS = ("refutation_tests", "refutation_test", "disproof_tests", "failure_tests")
BINDING_CONSTRAINT_FIELDS = (
    "binding_constraints",
    "hard_constraints",
    "active_constraints",
    "constraint_inventory",
)
CONSTRAINT_ROUTE_TERMS = (
    "constraint",
    "constrained",
    "hard constraint",
    "milp",
    "linear programming",
    "network flow",
    "slsqp",
    "least_squares",
    "optimization",
    "约束",
    "硬约束",
    "受约束",
    "优化",
    "规划",
    "网络流",
    "运力",
    "库存",
    "容量",
    "边界",
)
TRIGGER_TERMS = (
    "if ",
    "when ",
    "trigger",
    "deadline",
    "by day",
    "before ",
    "after ",
    "below",
    "above",
    "exceed",
    "如果",
    "若",
    "一旦",
    "触发",
    "截止",
    "低于",
    "高于",
    "超过",
    "不足",
)
ACTION_TERMS = (
    "switch",
    "fallback",
    "use ",
    "then ",
    "replace",
    "downgrade",
    "改用",
    "切换",
    "退回",
    "转为",
    "采用",
    "则",
)


def load_payload(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(payload, dict):
            raise SystemExit(f"Input JSON in {path} must be an object with a 'topics' list.")
        return payload
    except FileNotFoundError as exc:
        raise SystemExit(f"Input JSON not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def normalize_criteria(criteria: list[dict[str, Any]]) -> list[dict[str, Any]]:
    raw_items = []
    for index, item in enumerate(criteria, start=1):
        if not isinstance(item, dict):
            raise SystemExit(f"Criterion {index} must be an object.")
        if "key" not in item:
            raise SystemExit(f"Criterion {index} must include a 'key'.")
        if "weight" not in item:
            raise SystemExit(f"Criterion {item['key']} must include a 'weight'.")
        try:
            weight = float(item["weight"])
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"Criterion {item['key']} has non-numeric weight: {item['weight']!r}") from exc
        raw_items.append((item, weight))

    total = sum(weight for _, weight in raw_items)
    if total <= 0:
        raise SystemExit("Criteria weights must sum to a positive number.")

    normalized = []
    for item, weight in raw_items:
        normalized.append(
            {
                "key": item["key"],
                "label": item.get("label", item["key"]),
                "weight": weight / total,
                "description": item.get("description", ""),
            }
        )
    return normalized


def get_criteria(payload: dict[str, Any], name: str, defaults: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return normalize_criteria(payload.get(name) or defaults)


def get_blend(payload: dict[str, Any]) -> dict[str, float]:
    raw = payload.get("topic_route_blend") or DEFAULT_BLEND
    topic_weight = float(raw.get("topic_weight", DEFAULT_BLEND["topic_weight"]))
    route_weight = float(raw.get("route_weight", DEFAULT_BLEND["route_weight"]))
    total = topic_weight + route_weight
    if total <= 0:
        raise SystemExit("topic_route_blend weights must sum to a positive number.")
    return {"topic_weight": topic_weight / total, "route_weight": route_weight / total}


def get_route_question_blend(payload: dict[str, Any]) -> dict[str, float]:
    raw = payload.get("route_question_blend") or DEFAULT_ROUTE_QUESTION_BLEND
    route_weight = float(raw.get("route_weight", DEFAULT_ROUTE_QUESTION_BLEND["route_weight"]))
    question_chain_weight = float(
        raw.get("question_chain_weight", DEFAULT_ROUTE_QUESTION_BLEND["question_chain_weight"])
    )
    total = route_weight + question_chain_weight
    if total <= 0:
        raise SystemExit("route_question_blend weights must sum to a positive number.")
    return {"route_weight": route_weight / total, "question_chain_weight": question_chain_weight / total}


def get_team_fit_blend(payload: dict[str, Any]) -> dict[str, float] | None:
    team_profile = payload.get("team_profile")
    raw = payload.get("team_fit_blend")
    if raw is None and isinstance(team_profile, dict):
        raw = team_profile.get("team_fit_blend") or team_profile.get("blend")
    if raw is None:
        return None
    if raw is True:
        raw = DEFAULT_TEAM_FIT_BLEND
    if not isinstance(raw, dict):
        raise SystemExit("team_fit_blend must be an object when provided.")
    model_score_weight = float(raw.get("model_score_weight", DEFAULT_TEAM_FIT_BLEND["model_score_weight"]))
    team_fit_weight = float(raw.get("team_fit_weight", DEFAULT_TEAM_FIT_BLEND["team_fit_weight"]))
    total = model_score_weight + team_fit_weight
    if total <= 0:
        raise SystemExit("team_fit_blend weights must sum to a positive number.")
    return {"model_score_weight": model_score_weight / total, "team_fit_weight": team_fit_weight / total}


def score_entity(
    entity: dict[str, Any],
    criteria: list[dict[str, Any]],
    entity_label: str,
    require_decisive_support: bool = True,
    strict_criterion_support: bool = True,
) -> float:
    scores = entity.get("scores", {})
    if not isinstance(scores, dict):
        raise SystemExit(f"{entity_label} scores must be an object.")

    criterion_keys = {criterion["key"] for criterion in criteria}
    missing = [criterion["key"] for criterion in criteria if criterion["key"] not in scores]
    if missing:
        message = f"{entity_label} missing score(s): {', '.join(missing)}; treated as 0."
        entity.setdefault("_warnings", []).append(message)
        print(f"warning: {message}", file=sys.stderr)
    extra = [key for key in scores if key not in criterion_keys]
    if extra:
        message = f"{entity_label} has unrecognized score key(s): {', '.join(extra)}; ignored."
        entity.setdefault("_warnings", []).append(message)
        print(f"warning: {message}", file=sys.stderr)

    total = 0.0
    for criterion in criteria:
        score_was_provided = criterion["key"] in scores
        raw = scores.get(criterion["key"], 0)
        try:
            value = float(raw)
        except (TypeError, ValueError) as exc:
            raise SystemExit(
                f"{entity_label} has non-numeric score for {criterion['key']}: {raw!r}"
            ) from exc
        if not 0 <= value <= 5:
            raise SystemExit(f"{entity_label} score for {criterion['key']} must be between 0 and 5.")
        if (
            score_was_provided
            and require_decisive_support
            and (value >= DECISIVE_HIGH_SCORE or value <= DECISIVE_LOW_SCORE)
        ):
            criterion_label = criterion.get("label", criterion["key"])
            criterion_key = criterion["key"] if strict_criterion_support else None
            if not support_value(entity, EVIDENCE_FIELDS, criterion_key):
                entity.setdefault("_warnings", []).append(
                    f"{entity_label} has decisive {criterion_label} score {value:.1f} but no evidence field."
                )
            if not support_value(entity, FLIP_FIELDS, criterion_key):
                entity.setdefault("_warnings", []).append(
                    f"{entity_label} has decisive {criterion_label} score {value:.1f} but no flip_condition field."
                )
        total += value * criterion["weight"]
    return total


def default_question_role(index: int, total: int) -> str:
    if total <= 1:
        return "main/final"
    if total == 2:
        return "first" if index == 0 else "final"
    if total == 3:
        return ["first", "main", "final"][index]
    if index == 0:
        return "first"
    if index == 1:
        return "main"
    if index == total - 1:
        return "final"
    return "extend"


def default_question_weight(index: int, total: int) -> float:
    if total <= 1:
        return 1.0
    if total == 2:
        return [0.35, 0.65][index]
    if total == 3:
        return [0.20, 0.45, 0.35][index]
    if index == 0:
        return 0.15
    if index == 1:
        return 0.40
    if index == total - 1:
        return 0.15
    # Share the total extend-role weight across all middle extension questions.
    return 0.30 / max(total - 3, 1)


def get_question_weight(question: dict[str, Any], index: int, total: int) -> float:
    raw = question.get("question_weight", question.get("weight"))
    if raw is None:
        return default_question_weight(index, total)
    try:
        weight = float(raw)
    except (TypeError, ValueError) as exc:
        raise SystemExit(f"Question {question.get('name', index + 1)} weight must be numeric.") from exc
    if weight < 0:
        raise SystemExit(f"Question {question.get('name', index + 1)} weight must be non-negative.")
    return weight


def item_notes(item: dict[str, Any]) -> dict[str, Any]:
    notes = item.get("notes") or {}
    return notes if isinstance(notes, dict) else {}


def support_value(
    item: dict[str, Any],
    fields: tuple[str, ...],
    criterion_key: str | None = None,
    allow_any: bool = False,
) -> Any:
    notes = item_notes(item)
    containers = (item, notes)
    for field in fields:
        for container in containers:
            value = container.get(field)
            if not value:
                continue
            if isinstance(value, dict):
                if criterion_key and value.get(criterion_key):
                    return value[criterion_key]
                if criterion_key and not allow_any:
                    continue
                for generic_key in ("overall", "summary", "decisive", "decision", "final"):
                    if value.get(generic_key):
                        return value[generic_key]
                if allow_any:
                    for nested in value.values():
                        if nested:
                            return nested
                continue
            if criterion_key and not allow_any:
                continue
            return value
    return None


def fallback_value(item: dict[str, Any]) -> Any:
    return first_present(item, ("fallback", "fallback_plan", "rescue", "rescue_plan"))


def model_choice_value(item: dict[str, Any]) -> Any:
    return first_present(item, MODEL_CHOICE_FIELDS)


def rejected_alternatives_value(item: dict[str, Any]) -> Any:
    return first_present(item, REJECTED_ALTERNATIVE_FIELDS)


def refutation_value(item: dict[str, Any]) -> Any:
    return first_present(item, REFUTATION_FIELDS)


def binding_constraints_value(item: dict[str, Any]) -> Any:
    return first_present(item, BINDING_CONSTRAINT_FIELDS)


def crowd_escape_value(item: dict[str, Any]) -> Any:
    return first_present(item, CROWD_ESCAPE_FIELDS)


def flatten_text(value: Any) -> str:
    if not value:
        return ""
    if isinstance(value, str):
        return value.lower()
    if isinstance(value, dict):
        return " ".join(flatten_text(nested) for nested in value.values())
    if isinstance(value, list):
        return " ".join(flatten_text(nested) for nested in value)
    return str(value).lower()


def route_needs_binding_constraints(route: dict[str, Any]) -> bool:
    text = flatten_text(
        [
            route.get("main_model"),
            route.get("method"),
            route.get("model_choice_rationale"),
            route.get("solver"),
            route.get("validation"),
            route.get("refutation_tests"),
            route.get("rejected_alternatives"),
        ]
    )
    return any(term in text for term in CONSTRAINT_ROUTE_TERMS)


def team_fit_value(item: dict[str, Any]) -> float | None:
    raw = None
    if "team_fit_score" in item:
        raw = item.get("team_fit_score")
    elif isinstance(item.get("team_fit"), dict):
        raw = item["team_fit"].get("score")
    elif item.get("team_fit") is not None:
        raw = item.get("team_fit")
    if raw is None:
        return None
    try:
        value = float(raw)
    except (TypeError, ValueError) as exc:
        raise SystemExit(f"Topic {item.get('name', '<unnamed>')} team_fit score must be numeric.") from exc
    if not 0 <= value <= 5:
        raise SystemExit(f"Topic {item.get('name', '<unnamed>')} team_fit score must be between 0 and 5.")
    return value


def apply_team_fit_scores(ranked: list[dict[str, Any]], team_fit_blend: dict[str, float] | None) -> bool:
    if team_fit_blend is None:
        return False
    for topic in ranked:
        topic["_model_score"] = topic["_final_score"]
        topic["_team_fit_score"] = team_fit_value(topic)
        if topic["_team_fit_score"] is None:
            topic.setdefault("_warnings", []).append(
                f"Topic {topic.get('name', '<unnamed>')} missing team_fit score while team_fit_blend is enabled."
            )
            continue
        topic["_final_score"] = (
            topic["_model_score"] * team_fit_blend["model_score_weight"]
            + topic["_team_fit_score"] * team_fit_blend["team_fit_weight"]
        )
        topic["_score_mode"] = f"{topic['_score_mode']} + team fit"
    return True


def format_fallback(value: Any) -> str:
    if not value:
        return "-"
    if isinstance(value, dict):
        labels = (
            ("trigger", "trigger"),
            ("action", "action"),
            ("deadline", "deadline"),
        )
        parts = [f"{label}: {value[key]}" for key, label in labels if value.get(key)]
        if parts:
            return "; ".join(parts)
        return "; ".join(str(nested) for nested in value.values() if nested)
    if isinstance(value, list):
        return "; ".join(format_fallback(item) for item in value if item)
    return str(value)


def fallback_has_trigger_action(value: Any) -> bool:
    if not value:
        return False
    if isinstance(value, dict):
        return bool(value.get("trigger") and value.get("action"))
    if isinstance(value, list):
        return any(fallback_has_trigger_action(item) for item in value)
    text = str(value).lower()
    has_trigger = any(term in text for term in TRIGGER_TERMS)
    has_action = any(term in text for term in ACTION_TERMS)
    return has_trigger and has_action


def has_any_field(item: dict[str, Any], keys: tuple[str, ...]) -> bool:
    notes = item_notes(item)
    for key in keys:
        value = item.get(key, notes.get(key))
        if value:
            return True
    return False


def add_question_role_warnings(question: dict[str, Any], role: str, label: str) -> None:
    role_text = role.lower()
    if "first" in role_text and not has_any_field(question, ("baseline", "parameter_estimate", "simplified_case")):
        question.setdefault("_warnings", []).append(f"{label} is a first-role question but lacks a baseline or simplified case.")
    if "main" in role_text and not has_any_field(question, ("main_model", "upgrade", "method")):
        question.setdefault("_warnings", []).append(f"{label} is a main-role question but lacks a main model or upgrade.")
    if "extend" in role_text and not has_any_field(
        question, ("robustness", "scenario", "sensitivity", "validation")
    ):
        question.setdefault("_warnings", []).append(
            f"{label} is an extend-role question but lacks robustness, scenario, sensitivity, or validation design."
        )
    if "final" in role_text and not has_any_field(
        question, ("recommendation", "generalization", "final_deliverable", "decision")
    ):
        question.setdefault("_warnings", []).append(
            f"{label} is a final-role question but lacks recommendation, generalization, or decision output."
        )


def score_questions(route: dict[str, Any], question_criteria: list[dict[str, Any]], route_label: str) -> tuple[list[dict[str, Any]], float | None]:
    questions = route.get("questions") or route.get("question_chain") or []
    if not questions:
        return [], None
    if not isinstance(questions, list):
        raise SystemExit(f"{route_label} questions must be a list.")

    weight_flags = [
        isinstance(question, dict) and ("question_weight" in question or "weight" in question)
        for question in questions
    ]
    if any(weight_flags) and not all(weight_flags):
        route.setdefault("_warnings", []).append(
            f"{route_label} mixes explicit and default question weights; use all explicit weights or omit all weights."
        )

    scored_questions = []
    weighted_scores = []
    total = len(questions)
    for index, question in enumerate(questions):
        if not isinstance(question, dict):
            raise SystemExit(f"Question {index + 1} in {route_label} must be an object.")
        scored = dict(question)
        scored["_role"] = str(scored.get("role") or default_question_role(index, total))
        scored["_weight"] = get_question_weight(scored, index, total)
        label = f"Question {scored.get('name', index + 1)} in {route_label}"

        if isinstance(scored.get("scores"), dict) and scored["scores"]:
            scored["_score"] = score_entity(
                scored,
                question_criteria,
                label,
                strict_criterion_support=False,
            )
            if (
                scored["_score"] >= DECISIVE_HIGH_SCORE
                or scored["_score"] <= DECISIVE_LOW_SCORE
            ):
                if not support_value(scored, EVIDENCE_FIELDS, allow_any=True):
                    scored.setdefault("_warnings", []).append(
                        f"{label} has decisive question-chain score {scored['_score']:.2f} but no evidence field."
                    )
                if not support_value(scored, FLIP_FIELDS, allow_any=True):
                    scored.setdefault("_warnings", []).append(
                        f"{label} has decisive question-chain score {scored['_score']:.2f} but no flip_condition field."
                    )
            weighted_scores.append((scored["_score"], scored["_weight"]))
        else:
            scored["_score"] = None
            scored.setdefault("_warnings", []).append(
                f"{label} has no question scores; it is shown but not included in the question-chain score."
            )

        add_question_role_warnings(scored, scored["_role"], label)
        role_text = scored["_role"].lower()
        names_upgrade = has_any_field(scored, ("main_model", "upgrade")) or (
            "first" not in role_text and has_any_field(scored, ("method",))
        )
        if names_upgrade:
            if not model_choice_value(scored):
                scored.setdefault("_warnings", []).append(
                    f"{label} names a model or upgrade but lacks model_choice_rationale."
                )
            if not rejected_alternatives_value(scored):
                scored.setdefault("_warnings", []).append(
                    f"{label} names a model or upgrade but lacks rejected_alternatives."
                )
            if not refutation_value(scored):
                scored.setdefault("_warnings", []).append(
                    f"{label} names a model or upgrade but lacks refutation_tests."
                )
        question_fallback = fallback_value(scored)
        if question_fallback and not fallback_has_trigger_action(question_fallback):
            scored.setdefault("_warnings", []).append(
                f"{label} fallback should include a measurable trigger and action."
            )
        scored_questions.append(scored)

    weight_total = sum(weight for _, weight in weighted_scores)
    if weight_total <= 0:
        return scored_questions, None
    for question in scored_questions:
        if question.get("_score") is None:
            question["_effective_weight"] = None
        else:
            question["_effective_weight"] = question["_weight"] / weight_total
    question_chain_score = sum(score * weight for score, weight in weighted_scores) / weight_total
    return scored_questions, question_chain_score


def score_routes(
    topic: dict[str, Any],
    route_criteria: list[dict[str, Any]],
    question_criteria: list[dict[str, Any]],
    question_blend: dict[str, float],
) -> list[dict[str, Any]]:
    routes = topic.get("routes") or []
    if not isinstance(routes, list):
        raise SystemExit(f"Topic {topic.get('name', '<unnamed>')} routes must be a list.")

    scored_routes = []
    for index, route in enumerate(routes, start=1):
        if not isinstance(route, dict):
            raise SystemExit(f"Route {index} in topic {topic.get('name', '<unnamed>')} must be an object.")
        scored = dict(route)
        label = f"Route {route.get('name', index)} in topic {topic.get('name', '<unnamed>')}"
        base_score = score_entity(scored, route_criteria, label)
        route_names_model = has_any_field(scored, ("main_model", "method")) or bool(scored.get("scores"))
        if route_names_model:
            if not model_choice_value(scored):
                scored.setdefault("_warnings", []).append(
                    f"{label} names a route model but lacks model_choice_rationale."
                )
            if not rejected_alternatives_value(scored):
                scored.setdefault("_warnings", []).append(
                    f"{label} names a route model but lacks rejected_alternatives."
                )
            if not refutation_value(scored):
                scored.setdefault("_warnings", []).append(
                    f"{label} names a route model but lacks refutation_tests."
                )
        questions, question_chain_score = score_questions(scored, question_criteria, label)
        route_fallback = fallback_value(scored)
        if route_needs_binding_constraints(scored) and not binding_constraints_value(scored):
            scored.setdefault("_warnings", []).append(
                f"{label} appears to use constrained optimization or engineering constraints but lacks binding_constraints."
            )
        if not route_fallback:
            scored.setdefault("_warnings", []).append(
                f"{label} has no fallback; include trigger, action, and preferably deadline."
            )
        elif not fallback_has_trigger_action(route_fallback):
            scored.setdefault("_warnings", []).append(
                f"{label} fallback should include a measurable trigger and action."
            )
        scored["_base_score"] = base_score
        scored["_questions"] = questions
        scored["_question_chain_score"] = question_chain_score
        if question_chain_score is None:
            scored["_score"] = base_score
            scored["_route_score_mode"] = "route only"
        else:
            scored["_score"] = (
                base_score * question_blend["route_weight"]
                + question_chain_score * question_blend["question_chain_weight"]
            )
            scored["_route_score_mode"] = "route + question chain"
        scored_routes.append(scored)

    scored_routes.sort(key=lambda item: item["_score"], reverse=True)
    return scored_routes


def score_topic(
    topic: dict[str, Any],
    topic_criteria: list[dict[str, Any]],
    route_criteria: list[dict[str, Any]],
    question_criteria: list[dict[str, Any]],
    blend: dict[str, float],
    question_blend: dict[str, float],
) -> dict[str, Any]:
    scored = dict(topic)
    scored_routes = score_routes(topic, route_criteria, question_criteria, question_blend)
    has_topic_scores = isinstance(topic.get("scores"), dict) and bool(topic.get("scores"))

    topic_score = score_entity(scored, topic_criteria, f"Topic {topic.get('name', '<unnamed>')}") if has_topic_scores else None
    best_route_score = scored_routes[0]["_score"] if scored_routes else None

    if topic_score is None and best_route_score is None:
        raise SystemExit(
            f"Topic {topic.get('name', '<unnamed>')} must include topic scores, routes, or both."
        )
    if topic_score is not None and best_route_score is not None:
        final_score = topic_score * blend["topic_weight"] + best_route_score * blend["route_weight"]
        score_mode = "blended"
    elif topic_score is not None:
        final_score = topic_score
        score_mode = "topic only"
    else:
        final_score = best_route_score
        score_mode = "route only"

    scored["_topic_score"] = topic_score
    scored["_routes"] = scored_routes
    scored["_best_route_score"] = best_route_score
    scored["_final_score"] = final_score
    scored["_score_mode"] = score_mode
    return scored


def recommendation(score: float, rank: int, near_tie: bool = False, moderate_gap: bool = False) -> str:
    if rank == 1 and near_tie:
        return "co-primary / narrow lead"
    if rank == 1 and moderate_gap:
        return "primary lead / moderate uncertainty"
    if rank == 1 and score >= 4.2:
        return "primary choice"
    if rank == 1:
        return "primary among weak options"
    if score >= 4.2:
        return "strong fallback / co-primary if team-fit is better"
    if score >= 3.6:
        return "viable if the best route is executed well"
    if score >= 3.0:
        return "fallback only"
    return "avoid unless the team has special data or expertise"


def format_list(values: Any) -> str:
    if not values:
        return "-"
    if isinstance(values, str):
        return values
    return "; ".join(str(value) for value in values)


def cell(value: Any) -> str:
    text = "-" if value is None or value == "" else str(value)
    return text.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")


def score_text(value: float | None) -> str:
    return "-" if value is None else f"{value:.2f}"


def weight_text(value: float | None) -> str:
    return "-" if value is None else f"{value:.0%}"


def first_present(item: dict[str, Any], keys: tuple[str, ...]) -> Any:
    notes = item_notes(item)
    for key in keys:
        value = item.get(key, notes.get(key))
        if value:
            return value
    return None


def best_route_name(topic: dict[str, Any]) -> str:
    routes = topic.get("_routes") or []
    if not routes:
        return "-"
    return routes[0].get("name", "unnamed route")


def best_route(topic: dict[str, Any]) -> dict[str, Any] | None:
    routes = topic.get("_routes") or []
    return routes[0] if routes else None


def score_value(item: dict[str, Any], key: str) -> float | None:
    scores = item.get("scores") or {}
    if key not in scores:
        return None
    try:
        return float(scores[key])
    except (TypeError, ValueError):
        return None


def collect_comparison_warnings(
    ranked: list[dict[str, Any]], requires_question_chain: bool = False
) -> list[str]:
    warnings = []
    for topic in ranked:
        topic_name = topic.get("name", "<unnamed>")
        route = best_route(topic)
        if route:
            topic_diff = score_value(topic, "differentiation")
            route_diff = score_value(route, "route_differentiation")
            if topic_diff is not None and route_diff is not None:
                has_crowd_escape = crowd_escape_value(topic) or crowd_escape_value(route)
                if topic_diff <= 3.2 and route_diff >= 4.0:
                    if has_crowd_escape:
                        warnings.append(
                            f"{topic_name} has low topic differentiation but strong route differentiation; explain both layers separately."
                        )
                    else:
                        warnings.append(
                            f"{topic_name} has low topic differentiation but strong route differentiation and no crowd_escape_mechanism; name the route-level anti-homogeneity escape explicitly."
                        )
                if topic_diff >= 4.0 and route_diff <= 3.2:
                    warnings.append(
                        f"{topic_name} has high topic differentiation but weak route differentiation; do not let a novel domain mask a generic method route."
                    )
                if topic_diff > 3.2 and route_diff >= 4.0 and not has_crowd_escape:
                    warnings.append(
                        f"{topic_name} has moderate/high route differentiation but no crowd_escape_mechanism; popular topics need an explicit anti-homogeneity escape even when topic differentiation is only moderate."
                    )
            if requires_question_chain:
                for candidate_route in topic.get("_routes") or []:
                    if not candidate_route.get("_questions"):
                        route_name = candidate_route.get("name", "unnamed route")
                        warnings.append(
                            f"{topic_name} / {route_name} has no question_chain even though the payload marks the statements as fully stated."
                        )

    if len(ranked) >= 2:
        top_gap = ranked[0]["_final_score"] - ranked[1]["_final_score"]
        if top_gap <= 0.05:
            warnings.append(
                "Top two candidates are within 0.05 points; treat them as a near tie and choose by team strengths."
            )
        elif top_gap <= 0.20:
            warnings.append(
                "Top two candidates are within 0.20 points; treat the lead as moderate uncertainty unless decisive criteria have written evidence."
            )
        elif top_gap <= 0.20 + GAP_BOUNDARY_BUFFER:
            warnings.append(
                "Top two candidates are just above the 0.20 separation boundary; treat the lead as boundary-sensitive unless the decisive evidence survives refutation."
            )
        elif not (
            support_value(ranked[0], EVIDENCE_FIELDS, allow_any=True)
            and support_value(ranked[0], FLIP_FIELDS, allow_any=True)
        ):
            warnings.append(
                "Top candidate is separated by more than 0.20 points, but the topic lacks overall evidence or flip_condition."
            )
    return warnings


def score_gap_note(ranked: list[dict[str, Any]]) -> str:
    if len(ranked) < 2:
        return "Only one candidate was scored; no score gap comparison is available."
    gap = ranked[0]["_final_score"] - ranked[1]["_final_score"]
    if gap <= 0.05:
        return f"Near tie: top two candidates differ by {gap:.2f}; choose by team strengths and available data."
    if gap <= 0.20:
        return f"Moderate uncertainty: top two candidates differ by {gap:.2f}; require written decisive evidence before treating the lead as stable."
    if gap <= 0.20 + GAP_BOUNDARY_BUFFER:
        return f"Boundary-sensitive lead: top candidate leads by {gap:.2f}, just above 0.20; treat as moderate unless decisive evidence and team fit both survive refutation."
    evidence = support_value(ranked[0], EVIDENCE_FIELDS, allow_any=True)
    flip = support_value(ranked[0], FLIP_FIELDS, allow_any=True)
    if evidence and flip:
        return f"Evidence-backed separation: top candidate leads by {gap:.2f} and includes evidence plus flip condition."
    return f"Numerical separation: top candidate leads by {gap:.2f}, but evidence and flip condition must be written before the ranking is treated as decisive."


def collect_warnings(ranked: list[dict[str, Any]]) -> list[str]:
    warnings = []
    for topic in ranked:
        warnings.extend(topic.get("_warnings", []))
        for route in topic.get("_routes") or []:
            warnings.extend(route.get("_warnings", []))
            for question in route.get("_questions") or []:
                warnings.extend(question.get("_warnings", []))
    return warnings


def route_notes(route: dict[str, Any]) -> dict[str, Any]:
    notes = route.get("notes") or {}
    return notes if isinstance(notes, dict) else {}


def build_markdown(
    payload: dict[str, Any],
    topic_criteria: list[dict[str, Any]],
    route_criteria: list[dict[str, Any]],
    question_criteria: list[dict[str, Any]],
) -> str:
    topics = payload.get("topics") or []
    if not isinstance(topics, list) or not topics:
        raise SystemExit("Input JSON must contain a non-empty 'topics' list.")

    blend = get_blend(payload)
    question_blend = get_route_question_blend(payload)
    team_fit_blend = get_team_fit_blend(payload)
    ranked = [
        score_topic(topic, topic_criteria, route_criteria, question_criteria, blend, question_blend)
        for topic in topics
    ]
    team_fit_applied = apply_team_fit_scores(ranked, team_fit_blend)
    ranked.sort(key=lambda item: item["_final_score"], reverse=True)
    requires_question_chain = bool(
        payload.get("requires_question_chain")
        or payload.get("fully_stated")
        or payload.get("fully_stated_problems")
    )

    lines = []
    title = payload.get("contest") or "Mathematical Modeling Topic Selection"
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Score Gap Note")
    lines.append("")
    lines.append(score_gap_note(ranked))
    lines.append("")
    lines.append("## Topic Ranking")
    lines.append("")
    if team_fit_applied:
        lines.append(
            "| Rank | Candidate | Final | Mode | Model Score | Team Fit | Topic | Best Route | Best Route Score | Recommendation | Evidence | Flip Condition | Main Risk |"
        )
        lines.append("| ---: | --- | ---: | --- | ---: | ---: | ---: | --- | ---: | --- | --- | --- | --- |")
    else:
        lines.append(
            "| Rank | Candidate | Final | Mode | Topic | Best Route | Best Route Score | Recommendation | Evidence | Flip Condition | Main Risk |"
        )
        lines.append("| ---: | --- | ---: | --- | ---: | --- | ---: | --- | --- | --- | --- |")
    for index, topic in enumerate(ranked, start=1):
        notes = topic.get("notes") if isinstance(topic.get("notes"), dict) else {}
        route = best_route(topic)
        top_gap = topic["_final_score"] - ranked[1]["_final_score"] if index == 1 and len(ranked) >= 2 else None
        near_tie = top_gap is not None and top_gap <= 0.05
        moderate_gap = top_gap is not None and 0.05 < top_gap <= 0.20
        evidence = support_value(topic, EVIDENCE_FIELDS, allow_any=True)
        flip = support_value(topic, FLIP_FIELDS, allow_any=True)
        if route:
            evidence = evidence or support_value(route, EVIDENCE_FIELDS, allow_any=True)
            flip = flip or support_value(route, FLIP_FIELDS, allow_any=True)
        if team_fit_applied:
            lines.append(
                "| {rank} | {name} | {final} | {mode} | {model_score} | {team_fit} | {topic_score} | {route} | {route_score} | {rec} | {evidence} | {flip} | {risk} |".format(
                    rank=index,
                    name=cell(topic.get("name", f"Topic {index}")),
                    final=score_text(topic["_final_score"]),
                    mode=cell(topic["_score_mode"]),
                    model_score=score_text(topic.get("_model_score")),
                    team_fit=score_text(topic.get("_team_fit_score")),
                    topic_score=score_text(topic["_topic_score"]),
                    route=cell(best_route_name(topic)),
                    route_score=score_text(topic["_best_route_score"]),
                    rec=cell(recommendation(topic["_final_score"], index, near_tie, moderate_gap)),
                    evidence=cell(evidence),
                    flip=cell(flip),
                    risk=cell(format_list(topic.get("risks") or notes.get("risk"))),
                )
            )
        else:
            lines.append(
                "| {rank} | {name} | {final} | {mode} | {topic_score} | {route} | {route_score} | {rec} | {evidence} | {flip} | {risk} |".format(
                    rank=index,
                    name=cell(topic.get("name", f"Topic {index}")),
                    final=score_text(topic["_final_score"]),
                    mode=cell(topic["_score_mode"]),
                    topic_score=score_text(topic["_topic_score"]),
                    route=cell(best_route_name(topic)),
                    route_score=score_text(topic["_best_route_score"]),
                    rec=cell(recommendation(topic["_final_score"], index, near_tie, moderate_gap)),
                    evidence=cell(evidence),
                    flip=cell(flip),
                    risk=cell(format_list(topic.get("risks") or notes.get("risk"))),
                )
            )

    if any(topic.get("_topic_score") is not None for topic in ranked):
        lines.append("")
        lines.append("## Topic Scores")
        lines.append("")
        header = ["Candidate"] + [criterion["label"] for criterion in topic_criteria] + ["Topic Total"]
        lines.append("| " + " | ".join(cell(item) for item in header) + " |")
        lines.append("| " + " | ".join("---" for _ in header) + " |")
        for topic in ranked:
            row = [topic.get("name", "-")]
            scores = topic.get("scores") or {}
            for criterion in topic_criteria:
                row.append(scores.get(criterion["key"], "-"))
            row.append(score_text(topic["_topic_score"]))
            lines.append("| " + " | ".join(cell(item) for item in row) + " |")

    if any(topic.get("_routes") for topic in ranked):
        lines.append("")
        lines.append("## Method Route Rankings")
        for topic in ranked:
            routes = topic.get("_routes") or []
            if not routes:
                continue
            lines.append("")
            lines.append(f"### {cell(topic.get('name', 'Unnamed Topic'))}")
            lines.append("")
            lines.append(
                "| Rank | Route | Score | Mode | Core Method | Why This Model | Binding Constraints | Rejected Alternatives | Refutation Tests | Solver | Validation | Fallback | Evidence | Flip Condition | Highlight |"
            )
            lines.append("| ---: | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
            for index, route in enumerate(routes, start=1):
                notes = route_notes(route)
                lines.append(
                    "| {rank} | {name} | {score} | {mode} | {method} | {why} | {binding} | {rejected} | {refutation} | {solver} | {validation} | {fallback} | {evidence} | {flip} | {highlight} |".format(
                        rank=index,
                        name=cell(route.get("name", f"Route {index}")),
                        score=score_text(route["_score"]),
                        mode=cell(route.get("_route_score_mode")),
                        method=cell(route.get("main_model") or notes.get("method")),
                        why=cell(model_choice_value(route)),
                        binding=cell(format_list(binding_constraints_value(route))),
                        rejected=cell(format_list(rejected_alternatives_value(route))),
                        refutation=cell(format_list(refutation_value(route))),
                        solver=cell(route.get("solver") or notes.get("solver")),
                        validation=cell(route.get("validation") or notes.get("validation")),
                        fallback=cell(format_fallback(fallback_value(route))),
                        evidence=cell(support_value(route, EVIDENCE_FIELDS, allow_any=True)),
                        flip=cell(support_value(route, FLIP_FIELDS, allow_any=True)),
                        highlight=cell(notes.get("highlight") or route.get("superiority_claim")),
                    )
                )

    has_question_chains = any(
        question
        for topic in ranked
        for route in topic.get("_routes") or []
        for question in route.get("_questions") or []
    )
    if has_question_chains:
        lines.append("")
        lines.append("## Question Chain Scores")
        for topic in ranked:
            for route in topic.get("_routes") or []:
                questions = route.get("_questions") or []
                if not questions:
                    continue
                lines.append("")
                lines.append(f"### {cell(topic.get('name', 'Unnamed Topic'))} / {cell(route.get('name', 'Unnamed Route'))}")
                lines.append("")
                lines.append(
                    "Route base score: {base}; question-chain score: {chain}; final route score: {final}.".format(
                        base=score_text(route.get("_base_score")),
                        chain=score_text(route.get("_question_chain_score")),
                        final=score_text(route.get("_score")),
                    )
                )
                lines.append("")
                lines.append(
                    "| Question | Role | Effective Weight | Score | Deliverable | Baseline | Main/Upgrade | Why Chosen | Rejected Alternative | Refutation Test | Validation | Figure | Fallback/Dependency |"
                )
                lines.append("| --- | --- | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
                for index, question in enumerate(questions, start=1):
                    question_fallback = fallback_value(question)
                    fallback_dependency = [
                        format_fallback(question_fallback) if question_fallback else None,
                        first_present(question, ("supports_next", "dependency")),
                    ]
                    lines.append(
                        "| {name} | {role} | {weight} | {score} | {deliverable} | {baseline} | {upgrade} | {why} | {rejected} | {refutation} | {validation} | {figure} | {fallback_dependency} |".format(
                            name=cell(question.get("name", f"Q{index}")),
                            role=cell(question.get("_role")),
                            weight=cell(weight_text(question.get("_effective_weight"))),
                            score=score_text(question.get("_score")),
                            deliverable=cell(first_present(question, ("deliverable", "required_output", "target"))),
                            baseline=cell(first_present(question, ("baseline", "simplified_case"))),
                            upgrade=cell(first_present(question, ("main_model", "upgrade", "method"))),
                            why=cell(model_choice_value(question)),
                            rejected=cell(format_list(rejected_alternatives_value(question))),
                            refutation=cell(format_list(refutation_value(question))),
                            validation=cell(
                                first_present(question, ("validation", "sensitivity", "robustness", "scenario"))
                            ),
                            figure=cell(first_present(question, ("figure", "paper_figure", "table"))),
                            fallback_dependency=cell(format_list([value for value in fallback_dependency if value])),
                        )
                    )

    warnings = collect_warnings(ranked)
    warnings.extend(collect_comparison_warnings(ranked, requires_question_chain))
    warnings = list(dict.fromkeys(warnings))
    if warnings:
        lines.append("")
        lines.append("## Warnings")
        lines.append("")
        for warning in warnings:
            lines.append(f"- {cell(warning)}")

    lines.append("")
    lines.append("## Topic Criteria")
    lines.append("")
    for criterion in topic_criteria:
        percent = criterion["weight"] * 100
        lines.append(f"- {cell(criterion['label'])} ({percent:.1f}%): {cell(criterion['description'])}")

    lines.append("")
    lines.append("## Method Route Criteria")
    lines.append("")
    for criterion in route_criteria:
        percent = criterion["weight"] * 100
        lines.append(f"- {cell(criterion['label'])} ({percent:.1f}%): {cell(criterion['description'])}")

    if has_question_chains:
        lines.append("")
        lines.append("## Question Chain Criteria")
        lines.append("")
        for criterion in question_criteria:
            percent = criterion["weight"] * 100
            lines.append(f"- {cell(criterion['label'])} ({percent:.1f}%): {cell(criterion['description'])}")
        lines.append("")
        lines.append(
            "Routes with scored question chains blend route score and question-chain score "
            f"(route {question_blend['route_weight']:.0%}, question chain {question_blend['question_chain_weight']:.0%}). "
            "Routes without question scores remain route-only and should be treated as less audited, not automatically stronger."
        )

    lines.append("")
    lines.append(
        "Final score uses topic scores and best-route scores when both exist "
        f"(topic {blend['topic_weight']:.0%}, route {blend['route_weight']:.0%}); "
        "otherwise the Mode column shows whether the score is topic only or route only."
    )
    if team_fit_applied and team_fit_blend:
        lines.append(
            "When team_fit_blend is enabled, Final blends the model score and team-fit score "
            f"(model {team_fit_blend['model_score_weight']:.0%}, team fit {team_fit_blend['team_fit_weight']:.0%})."
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a weighted markdown comparison for contest topics and modeling routes."
    )
    parser.add_argument("input", type=Path, help="JSON file containing topics, scores, and optional routes.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional markdown output path. Prints to stdout if omitted.",
    )
    args = parser.parse_args()

    payload = load_payload(args.input)
    topic_criteria = get_criteria(payload, "topic_criteria", DEFAULT_TOPIC_CRITERIA)
    route_criteria = get_criteria(payload, "route_criteria", DEFAULT_ROUTE_CRITERIA)
    question_criteria = get_criteria(payload, "question_criteria", DEFAULT_QUESTION_CRITERIA)
    markdown = build_markdown(payload, topic_criteria, route_criteria, question_criteria)

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")


if __name__ == "__main__":
    main()
