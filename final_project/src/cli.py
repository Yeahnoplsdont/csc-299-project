import argparse
from .tasks import add_task, list_tasks, remove_task
from .ai_client import summarize_task_text

def main(argv=None):
    parser = argparse.ArgumentParser(prog="homework", description="Homework task manager")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add", help="Add a task")
    add.add_argument("--title", required=True)
    add.add_argument("--course", default="General")
    add.add_argument("--due", default="TBD")
    add.add_argument("--desc", default="")

    sub.add_parser("list", help="List tasks")

    sub.add_parser("summaries", help="Print AI summaries for tasks")
    
    remove = sub.add_parser("remove", help="Remove a task by title")
    remove.add_argument("--title", required =True)
    
    args = parser.parse_args(argv)

    if args.cmd == "add":
        task = add_task(args.title, args.course, args.due, args.desc)
        print("Added:", task)
    elif args.cmd == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks.")
            return
        for i, t in enumerate(tasks, 1):
            print(f"{i}. [{t.get('course')}] {t.get('title')} due {t.get('due')}")
    elif args.cmd == "summaries":
        tasks = list_tasks()
        if not tasks:
            print("No tasks.")
            return
        for i, t in enumerate(tasks, 1):
            summary = summarize_task_text(t.get("description", "") or t.get("title", ""))
            print(f"{i}. {t.get('title')} -> {summary}")

    elif args.cmd == "remove":
        success = remove_task(args.title)
        if success:
            print(f"Removed task: {args.title}")
        else:
            print(f"No task found with title: {args.title}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
