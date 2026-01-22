import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent_agree = models.BooleanField(
        label="Do you agree to participate in this study?",
        choices=[
            [True, "Yes, I agree"],
            [False, "No, I do not agree"],
        ],
    )


# PAGES
class Consent(Page):
    form_model = "player"
    form_fields = ["consent_agree"]

    @staticmethod
    def error_message(player, values):
        if values["consent_agree"] is False:
            return "You must agree to participate in order to continue."

    @staticmethod
    def before_next_page(player, timeout_happened):
        if "condition" not in player.participant.vars:
            player.participant.vars["condition"] = random.choice(["C1", "C2", "C3"])


page_sequence = [Consent]
