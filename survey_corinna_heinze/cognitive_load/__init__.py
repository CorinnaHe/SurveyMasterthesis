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
        choices=[i for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal,
    )


class CognitiveLoad(Page):
    form_model = "player"
    form_fields = ["cognitive_load_mental"]


page_sequence = [CognitiveLoad]