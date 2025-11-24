import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).resolve().parents[1] / "tasks.json"

def load_tasks() -> List[Dict]:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks: List[Dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def add_task(title: str, course: str, due: str, description: str) -> Dict:
    tasks = load_tasks()
    task = {"title": title, "course": course, "due": due, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    return task

def list_tasks() -> List[Dict]:
    return load_tasks()
