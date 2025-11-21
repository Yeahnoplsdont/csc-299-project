from tasks4 import summarize_task

def test_summarize_task_truncates():
    paragraph = "This is a very long task description that should be truncated for testing."
    summary = summarize_task(paragraph)
    assert len(summary) <= 35  # matches dummy truncate length
    assert "This is a very long task" in summary

def test_summarize_task_returns_string():
    paragraph = "Organize kitchen pantry"
    summary = summarize_task(paragraph)
    assert isinstance(summary, str)

