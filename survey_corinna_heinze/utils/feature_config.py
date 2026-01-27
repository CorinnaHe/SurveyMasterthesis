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
        "order": 4,
    },
    "feat_Monthly_Balance": {
        "label": "Monthly balance",
        "formatter": format_currency,
        "group": "Financial information",
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
        "order": 7,
    },
}
