# src/tasks3/__init__.py

def add_task(tasks, name):
    tasks.append({"name": name, "completed": False})
    return tasks

def complete_task(tasks, index):
    tasks[index]["completed"] = True
    return tasks

def main():
    print("This is the Task 3 PKMS app")

