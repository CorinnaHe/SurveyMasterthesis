from .formatting import (
    format_currency,
    format_percentage,
    format_int,
    format_string,
)

FEATURE_CONFIG = {
    "feat_Age": {
        "label": "Age",
        "formatter": format_int,
        "group": "Demographic information",
        "order": 1,
    },
    "feat_Occupation": {
        "label": "Occupation",
        "formatter": format_string,
        "group": "Demographic information",
        "order": 2,
    },
    "feat_Annual_Income": {
        "label": "Annual income",
        "formatter": format_currency,
        "group": "Financial information",
        "order": 3,
    },
    "feat_Outstanding_Debt": {
        "label": "Outstanding debt",
        "formatter": format_currency,
        "group": "Financial information",
        "explanation": "Total amount of outstanding financial liabilities.",
        "order": 4,
    },
    "feat_Monthly_Balance": {
        "label": "Monthly balance",
        "formatter": format_currency,
        "group": "Financial information",
        "explanation": "Average outstanding amount the applicant carries on a revolving credit account each month. "
                       "Higher values indicate heavier credit usage.",
        "order": 5,
    },
    "feat_Num_Credit_Card": {
        "label": "Number of credit cards",
        "formatter": format_int,
        "group": "Credit information",
        "order": 6,
    },
    "feat_Interest_Rate": {
        "label": "Interest rate",
        "formatter": format_percentage,
        "group": "Credit information",
        "explanation": "The percentage charged on the applicant’s existing credit, "
                       "which determines how much extra they have to pay on borrowed money over time. "
                       "A higher interest rate means borrowing is more expensive for the applicant.",
        "order": 7,
    },
}
