from otree.api import *
import csv
import random
from pathlib import Path

from trial_framework import (
    CONFIDENCE_LABELS,
    stage1_vars,
    stage2_vars,
)

TRIAL_LABEL = "Main Task"
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "tasks_main_trials.csv"

with open(DATA_FILE, encoding="utf-8") as f:
    TRIALS = list(csv.DictReader(f))


class C(BaseConstants):
    NAME_IN_URL = "main_trials"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 15


class Subsession(BaseSubsession):
    pass


def creating_session(session):
    for p in session.get_players():
        if "trial_order" not in p.participant.vars:
            indices = list(range(len(TRIALS)))
            random.shuffle(indices)
            p.participant.vars["trial_order"] = indices[:C.NUM_ROUNDS]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --- internal / analysis variables ---
    page_duration_stage1 = models.FloatField()
    page_duration_stage2 = models.FloatField()
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
        choices=list(CONFIDENCE_LABELS.items()),
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
        choices=list(CONFIDENCE_LABELS.items()),
        widget=widgets.RadioSelectHorizontal,
    )


def get_trial(player):
    order = player.participant.vars["trial_order"]
    return TRIALS[order[player.round_number - 1]]


class MainTrialsIntro(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Stage1(Page):
    form_model = "player"
    form_fields = ["initial_decision", "initial_confidence", "page_duration_stage1"]
    template_name = "trial_framework/Stage1.html"

    @staticmethod
    def vars_for_template(player):
        return stage1_vars(
            player,
            get_trial(player),
            trial_label=TRIAL_LABEL,
        )


class Stage2(Page):
    form_model = "player"
    form_fields = ["final_decision", "final_confidence", "page_duration_stage2"]
    template_name = "trial_framework/Stage2.html"

    @staticmethod
    def vars_for_template(player):
        return stage2_vars(
            player,
            get_trial(player),
            trial_label=TRIAL_LABEL,
        )


page_sequence = [MainTrialsIntro, Stage1, Stage2]
