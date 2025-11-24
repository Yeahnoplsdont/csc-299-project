from final_project.tasks import TaskStore

def test_add_and_load():
    store = TaskStore()
    store.tasks = []  # reset
    store.add_task("Test", "Course", "2025-12-01", "Demo")
    assert len(store.tasks) == 1
