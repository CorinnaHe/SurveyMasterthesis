from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'checks'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    check_decision_authority = models.IntegerField(
        label="Who makes the final decision in this task?",
        choices=[
            [1, "The AI system"],
            [2, "You, based only on your own judgment"],
            [3, "You, after the AI providing a recommendation"],
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

    # attempt counters
    attempts_decision_authority = models.IntegerField(initial=0)
    attempts_model_understanding = models.IntegerField(initial=0)

    # exit flag
    failed_checks = models.BooleanField(initial=False)


class Checks(Page):
    form_model = "player"
    form_fields = [
        "check_decision_authority",
        "check_model_understanding",
    ]

    @staticmethod
    def error_message(player, values):
        errors = {}

        # --- Question 1 ---
        if values["check_decision_authority"] != 3:
            attempts = player.field_maybe_none("attempts_decision_authority") or 0
            attempts += 1
            player.attempts_decision_authority = attempts

            if attempts > 1:
                player.failed_checks = True
                return None

            errors["check_decision_authority"] = (
                "This answer is incorrect. Please read the instructions again and try once more."
            )

        # --- Question 2 ---
        if values["check_model_understanding"] != 2:
            attempts = player.field_maybe_none("attempts_model_understanding") or 0
            attempts += 1
            player.attempts_model_understanding = attempts

            if attempts > 1:
                player.failed_checks = True
                return None

            errors["check_model_understanding"] = (
                "This answer is incorrect. Please review the explanation and try once more."
            )

        return errors


class FailedChecks(Page):
    @staticmethod
    def is_displayed(player):
        return player.failed_checks


page_sequence = [Checks, FailedChecks]
