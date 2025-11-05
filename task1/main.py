import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Enter task title: ")
    task = {"title": title}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!\n")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.\n")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']}")
    print()

def search_tasks():
    keyword = input("Enter search keyword: ").lower()
    tasks = load_tasks()
    matches = [t for t in tasks if keyword in t["title"].lower()]
    if not matches:
        print("No matching tasks found.\n")
        return
    print("Matches:")
    for i, task in enumerate(matches, 1):
        print(f"{i}. {task['title']}")
    print()

def main():
    while True:
        print("Options: add | list | search | exit")
        command = input("> ").strip().lower()

        if command == "add":
            add_task()
        elif command == "list":
            list_tasks()
        elif command == "search":
            search_tasks()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try again.\n")

if __name__ == "__main__":
    main()
