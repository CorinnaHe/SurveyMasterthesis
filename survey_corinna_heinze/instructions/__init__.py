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
class TasksInstructions(Page):
    form_model = "player"


class AIInstructions(Page):
    form_model = "player"

    @staticmethod
    def vars_for_template(player):
        return dict(
            condition=player.participant.vars["condition"],
            ai_label="➖ Standard creditworthiness",
            ai_correct_predictions=82,
            ai_incorrect_predictions=18,
            ai_confidence_level="high",
            cp_set_text="[➖ Standard creditworthiness, ✅ Good creditworthiness]",
            cp_coverage_correct=95,
            cp_coverage_incorrect=5,
        )

page_sequence = [TasksInstructions, AIInstructions]
