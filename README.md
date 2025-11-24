# Final Project — Homework Task Manager (final_project)

## Overview
A simple terminal-based homework task manager. Tasks are stored in a JSON file bundled with the package for the demo. The app optionally calls OpenAI to produce short summaries; if an API key or quota is not available it falls back to a deterministic local summary.

## Install & run (local)
Run inside repo root:

```bash
cd ~/Desktop/csc-299-project/final_project
source .venv/bin/activate
export PYTHONPATH=/Users/alanbadillo/Desktop/csc-299-project/final_project/src


# add a task
PYTHONPATH=src python -m final_project.cli add --title "HW1" --course "CS101" --due "2025-12-01" --desc "Read ch1"

# list tasks
PYTHONPATH=src python -m final_project.cli list

# show summaries
PYTHONPATH=src python -m final_project.cli summaries
