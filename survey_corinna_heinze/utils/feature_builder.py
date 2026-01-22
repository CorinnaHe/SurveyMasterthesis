from .feature_config import FEATURE_CONFIG


def build_display_features(trial):
    features = []

    for key, cfg in sorted(
        FEATURE_CONFIG.items(), key=lambda x: x[1]["order"]
    ):
        raw = trial.get(key)

        if raw in ["", None]:
            value = "–"
        else:
            value = cfg["formatter"](float(raw)) if raw.replace(".", "", 1).isdigit() else cfg["formatter"](raw)

        features.append({
            "label": cfg["label"],
            "value": value,
            "group": cfg["group"],
        })

    return features
