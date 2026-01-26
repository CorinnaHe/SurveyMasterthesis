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
    pass


# PAGES
class Instructions(Page):
    form_model = "player"

    @staticmethod
    def vars_for_template(player):
        return dict(
            condition=player.participant.vars["condition"]
        )


page_sequence = [Instructions]
