# Survey - Human Decision-Making with AI Support

This repository contains an online experiment built with **oTree 6** and managed using **Poetry**.

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

