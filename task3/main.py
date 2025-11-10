import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    name = input("Enter task name: ").strip()
    if not name:
        print("Task name cannot be empty.")
        return
    task = {"name": name, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Goals:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task.get("completed") else "❌"
        print(f"{i}. {task['name']} [{status}]")
    print()

def edit_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Enter task number to edit: ")) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid number.")
            return
        new_name = input("Enter new task name: ").strip()
        if new_name:
            tasks[idx]["name"] = new_name
            save_tasks(tasks)
            print("✏️ Task updated.")
        else:
            print("Task name cannot be empty.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid number.")
            return
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['name']}")
    except ValueError:
        print("Please enter a valid number.")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark complete: ")) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid number.")
            return
        tasks[idx]["completed"] = True
        save_tasks(tasks)
        print(f"🏁 Marked complete: {tasks[idx]['name']}")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("Options: add | list | edit | delete | complete | exit")
        cmd = input("> ").strip().lower()

        if cmd == "add":
            add_task(tasks)
        elif cmd == "list":
            list_tasks(tasks)
        elif cmd == "edit":
            edit_task(tasks)
        elif cmd == "delete":
            delete_task(tasks)
        elif cmd == "complete":
            complete_task(tasks)
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
