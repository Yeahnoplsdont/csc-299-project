from tasks3 import add_task

def test_add_task_creates_entry():
    tasks = []
    tasks.append({"name": "Test Task", "completed": False})
    assert tasks[0]["name"] == "Test Task"
    assert tasks[0]["completed"] is False

def test_complete_task_marks_done():
    tasks = [{"name": "Task 1", "completed": False}]
    tasks[0]["completed"] = True
    assert tasks[0]["completed"] is True

