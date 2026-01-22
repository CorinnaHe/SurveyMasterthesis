# Survey - Human Decision-Making with AI Support

This repository contains an online experiment built with **oTree 6** and managed using **Poetry**.

---

## Survey Flow
# Structure
````markdown
1. Consent 🖥️*1 page*
    1. Consent Info
    2. Consent Agree
2. Instructions 🖥️*1 page*
    1. Task Instructions
    2. 2 Stage Decision Process Explanation
    3. Check 1: Decision Authority
    4. Feature Overview
    5. Model Explanation (with SHAP values)
    6. Check 2: Model Understanding
    7. Condition Based Uncertainty Explanation
3. Example Trials (Number of Trials: 3)
    1. Intro Page 🖥️*1 page*
    2. Stage 1: Human-only initial Decision 🖥️*1 page*
        1. Features
        2. Initial Decision
        3. Initial Confidence
    3. Stage 2: AI Support + Final Decision 🖥️*1 page*
        1. Features + AI recommendation
        2. Final Decision
        3. Final Confidence
4. Manipulation Check 🖥️*1 page*
    1. Check 3: AI uncertainty communication
5. Main Trials (Number of Trials: 15, randomized)
    1. Intro Page 🖥️*1 page*
    2. Stage 1: Human-only initial Decision 🖥️*1 page*
        1. Features
        2. Initial Decision
        3. Initial Confidence
    3. Stage 2: AI Support + Final Decision 🖥️*1 page*
        1. Features + AI recommendation
        2. Final Decision
        3. Final Confidence
6. Cognitive Load 🖥️*1 page*
    1. 1 - 3 Questions
7. Control Measures 🖥️*1 page*
8. Closing 🖥️*1 page*
````
---

## Requirements

* Python **3.11**
* Poetry ([https://python-poetry.org/](https://python-poetry.org/))
* oTree **6.x**

---

## Setup

### 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
cd <PROJECT_FOLDER>
```

---

### 2. Install dependencies with Poetry

```bash
poetry install
```

This creates a virtual environment and installs all required packages.

---

### 3. Activate the Poetry environment (optional)

```bash
poetry shell
```

*(All commands below also work without this if you prefix them with `poetry run`.)*

---

## Running the experiment (development)

### Start the oTree development server

```bash
poetry run otree devserver
```

Then open your browser at:

```
http://localhost:8000
```

---

### Reset the database (important after model changes)

Whenever you change model fields (e.g., add questions):

```bash
poetry run otree resetdb
```

⚠️ This deletes all existing sessions and data.

---

## Common oTree commands

| Purpose          | Command                                |
| ---------------- | -------------------------------------- |
| Start dev server | `poetry run otree devserver`           |
| Reset database   | `poetry run otree resetdb`             |
| Open oTree shell | `poetry run otree shell`               |
| Create a new app | `poetry run otree startapp <app_name>` |

---

## Project structure (simplified)

```text
.
├── settings.py
├── pyproject.toml
├── consent/
├── instructions/
├── example_trials/
├── manipulation_check/
├── main_trials/
├── cognitive_load/
├── control_measures/
├── closing/
└── README.md
```

Each app contains:

* `__init__.py` (models + pages, oTree 6 style)
* `*.html` (HTML templates)

---

## Notes

* The project uses **participant-level condition assignment** stored in `participant.vars`.
* Trial tasks are loaded from CSV files inside the corresponding app folders.

