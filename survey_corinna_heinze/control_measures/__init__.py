from otree.api import *

LIKERT_0_10_LITERACY = [i for i in range (0, 11)]


class C(BaseConstants):
    NAME_IN_URL = 'control_measures'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # -----------------
    # Demographics
    # -----------------

    age = models.IntegerField(
        label="What is your age?",
        min=18,
        max=90,
    )

    gender = models.StringField(
        label="What is your gender?",
        choices=[
            "Female",
            "Male",
            "Non-binary / third gender",
            "Prefer not to say",
        ],
        widget=widgets.RadioSelect,
    )

    education = models.StringField(
        label="What is the highest level of education you have completed?",
        choices=[
            "Secondary school",
            "Bachelor’s degree",
            "Master’s degree",
            "Doctorate",
            "Other",
        ],
        widget=widgets.RadioSelect,
    )

    # -----------------
    # AI literacy (0–10)
    # -----------------

    ai_literacy1 = models.IntegerField(
        label="I am familiar with AI-based applications that are used in everyday life.",
        choices=LIKERT_0_10_LITERACY,
        widget=widgets.RadioSelectHorizontal,
    )

    ai_literacy2 = models.IntegerField(
        label="I can use AI-based applications to support my decisions in everyday situations.",
        choices=LIKERT_0_10_LITERACY,
        widget=widgets.RadioSelectHorizontal,
    )

    ai_literacy3 = models.IntegerField(
        label="I understand that AI systems have both strengths and limitations.",
        choices=LIKERT_0_10_LITERACY,
        widget=widgets.RadioSelectHorizontal,
    )

    ai_literacy4 = models.IntegerField(
        label="I can usually tell when a system or service is based on artificial intelligence.",
        choices=LIKERT_0_10_LITERACY,
        widget=widgets.RadioSelectHorizontal,
    )

    # -----------------
    # Risk aversion (SOEP)
    # -----------------

    risk_aversion = models.IntegerField(
        label=(
            "How do you see yourself? Are you generally a person who is fully prepared "
            "to take risks or do you try to avoid taking risks? "
            "Please tick a box on the scale"
        ),
        choices=[i for i in range(1,8)],
        widget=widgets.RadioSelectHorizontal,
    )

    # -----------------
    # Domain experience
    # -----------------

    domain_experience = models.StringField(
        label=(
            "Do you have any prior experience with credit-related decision tasks "
            "(e.g., credit evaluations, financial risk assessments)?"
        ),
        choices=[
            "No experience",
            "Some familiarity",
            "Professional experience",
        ],
        widget=widgets.RadioSelect,
    )


    # -----------------
    # Comment
    # -----------------
    comment = models.LongStringField(
        label="Optional: If you would like to comment on anything, you can do so here.",
        blank=True
    )


class ControlMeasures(Page):
    form_model = "player"
    form_fields = [
        "age",
        "gender",
        "education",
        "ai_literacy1",
        "ai_literacy2",
        "ai_literacy3",
        "ai_literacy4",
        "risk_aversion",
        "domain_experience",
        "comment",
    ]


page_sequence = [ControlMeasures]
