# trial_common.py
from utils import build_display_features

DECISION_LABELS = {
    1: "❌ Poor creditworthiness",
    2: "➖ Standard creditworthiness",
    3: "✅ Good creditworthiness",
}

AI_LABEL_MAP = {
    "poor": "❌ Poor creditworthiness",
    "standard": "➖ Standard creditworthiness",
    "good": "✅ Good creditworthiness",
}


def initialize_player_from_trial(player, trial):
    """
    Store trial-specific values exactly once.
    """
    if player.field_maybe_none("case_id") is not None:
        return

    player.case_id = int(trial["case_id"])
    player.y_true = trial["y_true"]

    player.point_pred_cal = trial["point_pred_cal"]
    player.point_pred_confidence = float(
        trial["point_pred_confidence_cal_prediction"]
    )

    player.cp_contains_good = trial["cp_standard_contains_good"] == "True"
    player.cp_contains_poor = trial["cp_standard_contains_poor"] == "True"
    player.cp_contains_standard = trial["cp_standard_contains_standard"] == "True"


def stage1_vars(player, trial, trial_label):
    initialize_player_from_trial(player, trial)
    return dict(
        trial_number=player.round_number,
        trial=trial,
        features=build_display_features(trial),
        trial_label=trial_label
    )


def stage2_vars(player, trial, trial_label):
    cp_labels = []
    if player.cp_contains_good:
        cp_labels.append("✅ Good creditworthiness")
    if player.cp_contains_standard:
        cp_labels.append("➖ Standard creditworthiness")
    if player.cp_contains_poor:
        cp_labels.append("❌ Poor creditworthiness")

    ai_correct = int(round(player.point_pred_confidence * 100))

    return dict(
        trial_number=player.round_number,
        trial=trial,
        trial_label=trial_label,
        features=build_display_features(trial),
        condition=player.participant.vars["condition"],

        initial_decision_label=DECISION_LABELS[player.initial_decision],

        ai_label = AI_LABEL_MAP.get(player.point_pred_cal, player.point_pred_cal),
        ai_correct_predictions=ai_correct,
        ai_incorrect_predictions=100 - ai_correct,
        ai_confidence_level=trial["confidence_bin_point_pred"].split("_", 1)[0],

        cp_set_text=trial["cp_standard_sorted_set"],
        cp_coverage_correct=95,
        cp_coverage_incorrect=5,
    )
