from .feature_config import FEATURE_CONFIG


def build_display_features(trial):
    features = []

    sorted_features = sorted(
        FEATURE_CONFIG.items(),
        key=lambda x: x[1]["order"]
    )

    for key, cfg in sorted_features:
        raw = trial.get(key)

        if raw in ["", None]:
            value = "–"
        else:
            if isinstance(raw, (int, float)):
                value = cfg["formatter"](raw)
            elif isinstance(raw, str) and raw.replace(".", "", 1).isdigit():
                value = cfg["formatter"](float(raw))
            else:
                value = cfg["formatter"](raw)

        features.append({
            "label": cfg["label"],
            "value": value,
            "group": cfg["group"],
        })

    return features
