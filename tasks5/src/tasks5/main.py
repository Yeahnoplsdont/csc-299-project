from specify_cli import TaskManager

def main():
    # Initialize a task manager
    tm = TaskManager()

    # Add some demo tasks
    tm.add_task("Finish CSC 299 Task 5")
    tm.add_task("Push Task 5 to GitHub")

    # List all tasks
    print("Tasks:")
    for task in tm.list_tasks():
        print(f"- {task}")

    # Complete a task
    tm.complete_task("Push Task 5 to GitHub")
    print("\nAfter completing a task:")
    for task in tm.list_tasks():
        print(f"- {task}")

if __name__ == "__main__":
    main()

