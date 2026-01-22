from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'manipulation_check'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    manipulation_check = models.IntegerField(
        label="How did the AI communicate its assessment in this task?",
        choices=[
            [1, "Single outcome, no uncertainty information"],
            [2, "Single outcome + frequency-based uncertainty"],
            [3, "Multiple plausible outcomes + coverage frequency"],
        ],
        widget=widgets.RadioSelect,
    )


class ManipulationCheck(Page):
    form_model = "player"
    form_fields = ["manipulation_check"]

    @staticmethod
    def vars_for_template(player):
        return dict(
            condition=player.participant.vars["condition"]
        )

    @staticmethod
    def error_message(player, values):
        condition = player.participant.vars["condition"]

        correct_answer = {
            "C1": 1,
            "C2": 2,
            "C3": 3,
        }[condition]

        if values["manipulation_check"] != correct_answer:
            return "Please review the previous instructions carefully and try again."


page_sequence = [ManipulationCheck]
