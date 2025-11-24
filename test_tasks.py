import os
from pathlib import Path
import pytest
from final_project.tasks import add_task, list_tasks, save_tasks, load_tasks
from final_project.ai_client import summarize_task_text

def test_add_and_list(tmp_path, monkeypatch):
    # create temporary tasks.json in package src
    tmp_data = tmp_path / "tasks.json"
    monkeypatch.chdir(tmp_path)
    # ensure empty
    assert list_tasks() == []
    add_task("Read Chapter 1", "CS101", "2025-12-01", "Read pages 1-30")
    tasks = list_tasks()
    assert tasks and tasks[-1]["title"] == "Read Chapter 1"

def test_summarize_fallback(monkeypatch):
    # ensure no API key and OpenAI not available -> deterministic fallback
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    s = summarize_task_text("This is a long description that should be truncated for testing purposes.")
    assert isinstance(s, str)
    assert len(s) <= 63 or s.endswith("...")
