from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # comprehension checks
    check_decision_authority = models.IntegerField(
        label="Who makes the final decision in this task?",
        choices=[
            [1, "The AI system"],
            [2, "You, based only on your own judgment"],
            [3, "You, with the AI providing a recommendation"],
            [4, "The system automatically combines your answer with the AI"],
        ],
        widget=widgets.RadioSelect,
    )

    check_model_understanding = models.IntegerField(
        label="According to the explanation, which factors had the strongest influence on the AI’s assessment across cases?",
        choices=[
            [1, "Monthly Income"],
            [2, "Interest Rate"],
            [3, "Age"],
        ],
        widget=widgets.RadioSelect,
    )


# PAGES
class Instructions(Page):
    form_model = "player"
    form_fields = [
        "check_decision_authority",
        "check_model_understanding",
    ]

    @staticmethod
    def error_message(player, values):
        errors = {}
        if values["check_decision_authority"] != 3:
            errors["check_decision_authority"] = "Please read the instructions carefully and select the correct answer."
        if values["check_model_understanding"] != 2:
            errors["check_model_understanding"] = "Please select the correct answer based on the explanation above."
        return errors

    @staticmethod
    def vars_for_template(player):
        return dict(
            condition=player.participant.vars["condition"]
        )


page_sequence = [Instructions]
