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
            [2, "You, after the AI providing a recommendation"],
            [3, "The system automatically combines your answer with the AI"],
        ],
        widget=widgets.RadioSelect,
    )

    check_task_domain = models.IntegerField(
        label="In this task, you take the role of a:",
        choices=[
            [1, "Bank Employee"],
            [2, "Student"],
            [3, "Doctor"],
        ],
        widget=widgets.RadioSelect,
    )

    # attempt counters
    attempts_decision_authority = models.IntegerField(initial=0)
    attempts_task_domain = models.IntegerField(initial=0)

    # exit flag
    failed_checks = models.BooleanField(initial=False)


class Checks(Page):
    form_model = "player"
    form_fields = [
        "check_decision_authority",
        "check_task_domain",
    ]

    @staticmethod
    def error_message(player, values):
        errors = {}

        # --- Question 1 ---
        if values["check_decision_authority"] != 2:
            attempts = player.field_maybe_none("attempts_decision_authority") or 0
            attempts += 1
            player.attempts_decision_authority = attempts

            if attempts > 1:
                player.failed_checks = True
                return None

            errors["check_decision_authority"] = (
                "This answer is incorrect. Please try once more."
            )

        # --- Question 2 ---
        if values["check_task_domain"] != 1:
            attempts = player.field_maybe_none("check_task_domain") or 0
            attempts += 1
            player.attempts_task_domain = attempts

            if attempts > 1:
                player.failed_checks = True
                return None

            errors["check_task_domain"] = (
                "This answer is incorrect. Please try once more."
            )

        return errors


class FailedChecks(Page):
    @staticmethod
    def is_displayed(player):
        return player.failed_checks


page_sequence = [Checks, FailedChecks]
