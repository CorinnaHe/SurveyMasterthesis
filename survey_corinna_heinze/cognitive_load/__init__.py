from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'cognitive_load'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    cognitive_load_mental = models.IntegerField(
        label="How much mental effort did you invest in this task?",
        choices=[
            [1, "1 - Very low mental effort"],
            [2, "2 - Low mental effort"],
            [3, "3 - Rather low mental effort"],
            [4, "4 - Neither low nor high mental effort"],
            [5, "5 - Rather high mental effort"],
            [6, "6 - High mental effort"],
            [7, "7 - Very high mental effort"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )


class CognitiveLoad(Page):
    form_model = "player"
    form_fields = ["cognitive_load_mental"]


page_sequence = [CognitiveLoad]