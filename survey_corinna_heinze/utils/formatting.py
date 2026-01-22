def format_currency(value):
    return f"${value:,.0f}"


def format_percentage(value):
    return f"{int(value)} %"


def format_int(value):
    return str(int(value))


def format_string(value):
    return value.replace("_", " ")
