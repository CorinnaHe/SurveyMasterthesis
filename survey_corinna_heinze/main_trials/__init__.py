from otree.api import *
from pathlib import Path
import csv
import random

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "tasks_main_trials.csv"

with open(DATA_FILE, encoding="utf-8") as f:
    TRIALS = list(csv.DictReader(f))

DECISION_LABELS = {
    1: "Poor creditworthiness",
    2: "Standard creditworthiness",
    3: "Good creditworthiness",
}

CONFIDENCE_LABELS = {
    1: "Not confident at all",
    2: "Slightly confident",
    3: "Moderately confident",
    4: "Very confident",
    5: "Completely confident",
}


class C(BaseConstants):
    NAME_IN_URL = 'main_trials'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 15


class Subsession(BaseSubsession):
    pass


def creating_session(Session):
    for p in Session.get_players():
        if "trial_order" not in p.participant.vars:
            indices = list(range(len(TRIALS)))
            random.shuffle(indices)

            # keep only as many as needed
            p.participant.vars["trial_order"] = indices[:C.NUM_ROUNDS]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --- internal / analysis variables ---
    case_id = models.IntegerField(blank=True)
    y_true = models.StringField(blank=True)

    point_pred_cal = models.StringField(blank=True)
    point_pred_confidence = models.FloatField(blank=True)

    cp_contains_good = models.BooleanField(blank=True)
    cp_contains_poor = models.BooleanField(blank=True)
    cp_contains_standard = models.BooleanField(blank=True)

    # -------- Stage 1 --------
    initial_decision = models.IntegerField(
        label="How would you classify this applicant’s creditworthiness?",
        choices=[
            [1, "Poor creditworthiness"],
            [2, "Standard creditworthiness"],
            [3, "Good creditworthiness"],
        ],
        widget=widgets.RadioSelect,
    )

    initial_confidence = models.IntegerField(
        label="How confident are you in your decision?",
        choices=[
            [1, "Not confident at all"],
            [2, "Slightly confident"],
            [3, "Moderately confident"],
            [4, "Very confident"],
            [5, "Completely confident"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    # -------- Stage 2 --------
    final_decision = models.IntegerField(
        label="Please make your final decision, taking into account the applicant information and the AI assessment.",
        choices=[
            [1, "Poor creditworthiness"],
            [2, "Standard creditworthiness"],
            [3, "Good creditworthiness"],
        ],
        widget=widgets.RadioSelect,
    )

    final_confidence = models.IntegerField(
        label="How confident are you in your final decision?",
        choices=[
            [1, "Not confident at all"],
            [2, "Slightly confident"],
            [3, "Moderately confident"],
            [4, "Very confident"],
            [5, "Completely confident"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )


def get_trial(player):
    """
    Maps round_number -> randomized CSV row for this participant.
    """
    order = player.participant.vars["trial_order"]
    row_index = order[player.round_number - 1]
    return TRIALS[row_index]


# --------------------
# Intro Page
# --------------------
class MainTrialsIntro(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


# --------------------
# Stage 1 Page
# --------------------
class Stage1(Page):
    form_model = "player"
    form_fields = ["initial_decision", "initial_confidence"]

    @staticmethod
    def vars_for_template(player):
        trial = get_trial(player)

        # store internal values once
        if player.field_maybe_none("case_id") is None:
            player.case_id = int(trial["case_id"])
            player.y_true = trial["y_true"]

            player.point_pred_cal = trial["point_pred_cal"]
            player.point_pred_confidence = float(
                trial["point_pred_confidence_cal_prediction"]
            )

            player.cp_contains_good = trial["cp_standard_contains_good"] == "True"
            player.cp_contains_poor = trial["cp_standard_contains_poor"] == "True"
            player.cp_contains_standard = trial["cp_standard_contains_standard"] == "True"

        return dict(
            trial_number=player.round_number,
            trial=trial,
        )


# --------------------
# Stage 2 Page
# --------------------
class Stage2(Page):
    form_model = "player"
    form_fields = ["final_decision", "final_confidence"]

    @staticmethod
    def vars_for_template(player):
        trial = get_trial(player)

        initial_decision_label = DECISION_LABELS.get(player.initial_decision)
        initial_confidence_label = CONFIDENCE_LABELS.get(player.initial_confidence)

        # build CP set labels
        cp_labels = []
        if player.cp_contains_good:
            cp_labels.append("Good creditworthiness")
        if player.cp_contains_standard:
            cp_labels.append("Standard creditworthiness")
        if player.cp_contains_poor:
            cp_labels.append("Poor creditworthiness")

        cp_set_text = ", ".join(cp_labels)

        ai_correct_predictions = int(round(player.point_pred_confidence * 100))
        ai_incorrect_predictions = 100 - ai_correct_predictions

        return dict(
            trial_number=player.round_number,
            trial=trial,
            condition=player.participant.vars["condition"],

            # initial responses
            initial_decision_label=initial_decision_label,
            initial_confidence_label=initial_confidence_label,

            # AI outputs
            ai_label=player.point_pred_cal,
            ai_correct_predictions=ai_correct_predictions,
            ai_incorrect_predictions=ai_incorrect_predictions,

            # CP (READY FOR DISPLAY)
            cp_set_text=cp_set_text,
        )


page_sequence = [MainTrialsIntro, Stage1, Stage2]