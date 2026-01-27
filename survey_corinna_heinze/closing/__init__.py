import re

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'closing'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    contact_email = models.StringField(
        blank=True,
        label="Email address (optional, for voucher delivery only)"
    )
    num_correct_final = models.IntegerField()


class Closing(Page):
    form_model = "player"
    form_fields = ["contact_email"]

    @staticmethod
    def vars_for_template(player):
        player.num_correct_final = player.participant.vars.get("num_correct_final", 0)
        num_correct = player.participant.vars.get("num_correct_final", 0)

        return dict(
            num_correct=num_correct,
            num_total=15,
        )

    @staticmethod
    def error_message(player, values):
        email = values.get("contact_email")

        # Case 1: Submit pressed without email
        if not email:
            return (
                "Providing an email address is optional. "
                "However, if you wish to participate in the voucher incentive, "
                "please enter an email address. "
                "If you do not wish to participate in the incentive, "
                "you may simply close this page without submitting."
            )

        # Case 2: Email entered but invalid format
        email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(email_regex, email):
            return (
                "Please enter a valid email address (for example: name@example.com). "
                "The address you entered does not appear to be valid."
            )


page_sequence = [Closing]
