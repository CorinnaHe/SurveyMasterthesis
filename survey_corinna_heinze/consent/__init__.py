import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(self):
    if 'condition_counter' not in self.session.vars:
        self.session.vars['condition_counter'] = 0


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
    condition = models.StringField()


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
            counter = player.session.vars['condition_counter']

            conditions = ["C1", "C2", "C3"]
            assigned_condition = conditions[counter % len(conditions)]

            player.condition = assigned_condition
            player.participant.vars["condition"] = assigned_condition
            player.session.vars['condition_counter'] += 1


page_sequence = [Consent]
