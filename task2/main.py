#!/usr/bin/env python3
import json
import os
from datetime import datetime

FILENAME = "goals.json"
DATE_FORMAT = "%Y-%m-%d"

def load_goals():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_goals(goals):
    with open(FILENAME, "w") as file:
        json.dump(goals, file, indent=4)

def parse_date(date_str):
    """Return a datetime.date or None if invalid/empty."""
    date_str = date_str.strip()
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        return None

def format_date(date_obj):
    return date_obj.isoformat() if date_obj else "No due date"

def add_goal():
    name = input("Goal name: ").strip()
    if not name:
        print("Goal name cannot be empty.\n")
        return
    description = input("Description: ").strip()
    due_raw = input(f"Due date ({DATE_FORMAT} or leave blank): ").strip()
    due = parse_date(due_raw)
    goal = {
        "name": name,
        "description": description,
        "due": due.isoformat() if due else "",
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    goals = load_goals()
    goals.append(goal)
    save_goals(goals)
    print("✅ Goal added!\n")

def list_goals(goals=None, show_index=True):
    if goals is None:
        goals = load_goals()
    if not goals:
        print("No goals found.\n")
        return
    today = datetime.now().date()
    for i, g in enumerate(goals, start=1):
        status = "✅" if g.get("completed") else "❌"
        due_date = parse_date(g.get("due", "")) 
        due_text = format_date(due_date)
        overdue = ""
        if due_date and not g.get("completed") and due_date < today:
            overdue = " (OVERDUE)"
        idx = f"{i}. " if show_index else ""
        print(f"{idx}{g.get('name')} — {g.get('description')} — Due: {due_text} {overdue} [{status}]")
    print()

def search_goal():
    term = input("Search by name or description: ").lower().strip()
    if not term:
        print("Enter a search term.\n")
        return
    goals = load_goals()
    results = [g for g in goals if term in g.get("name","").lower() or term in g.get("description","").lower()]
    if not results:
        print("No matching goals.\n")
        return
    list_goals(results, show_index=False)

def complete_goal():
    goals = load_goals()
    if not goals:
        print("No goals to complete.\n")
        return
    list_goals(goals)
    try:
        idx = int(input("Enter goal number to mark complete: ").strip()) - 1
    except ValueError:
        print("Please enter a number.\n")
        return
    if 0 <= idx < len(goals):
        goals[idx]["completed"] = True
        save_goals(goals)
        print("🎉 Goal marked complete!\n")
    else:
        print("Invalid goal number.\n")

def delete_goal():
    goals = load_goals()
    if not goals:
        print("No goals to delete.\n")
        return
    list_goals(goals)
    try:
        idx = int(input("Enter goal number to delete: ").strip()) - 1
    except ValueError:
        print("Please enter a number.\n")
        return
    if 0 <= idx < len(goals):
        removed = goals.pop(idx)
        save_goals(goals)
        print(f"Removed goal: {removed.get('name')}\n")
    else:
        print("Invalid goal number.\n")

def edit_goal():
    goals = load_goals()
    if not goals:
        print("No goals to edit.\n")
        return
    list_goals(goals)
    try:
        idx = int(input("Enter goal number to edit: ").strip()) - 1
    except ValueError:
        print("Please enter a number.\n")
        return
    if not (0 <= idx < len(goals)):
        print("Invalid goal number.\n")
        return

    g = goals[idx]
    print("Press Enter to keep current value.")
    new_name = input(f"Name [{g.get('name')}]: ").strip()
    if new_name:
        g["name"] = new_name
    new_desc = input(f"Description [{g.get('description')}]: ").strip()
    if new_desc:
        g["description"] = new_desc
    new_due_raw = input(f"Due date ({DATE_FORMAT}) [{g.get('due') or 'blank'}]: ").strip()
    if new_due_raw != "":
        new_due = parse_date(new_due_raw)
        if new_due is None and new_due_raw != "":
            print("Invalid date format — keeping existing due date.")
        else:
            g["due"] = new_due.isoformat() if new_due else ""
    save_goals(goals)
    print("Goal updated.\n")

def sort_goals_by_due(ascending=True):
    goals = load_goals()
    # Convert due to date or None, then sort
    def due_key(g):
        d = parse_date(g.get("due",""))
        # None should go to end if ascending, beginning if descending:
        return (d is None, d) if ascending else (d is not None, d if d else datetime.min.date())
    sorted_goals = sorted(goals, key=due_key)
    list_goals(sorted_goals)

def filter_by_status():
    goals = load_goals()
    choice = input("Filter by status (all / complete / incomplete): ").strip().lower()
    if choice == "complete":
        results = [g for g in goals if g.get("completed")]
    elif choice == "incomplete":
        results = [g for g in goals if not g.get("completed")]
    else:
        results = goals
    list_goals(results)

def show_help():
    print("Commands:")
    print("  add       - Add a new goal")
    print("  list      - List all goals")
    print("  search    - Search goals by name/description")
    print("  complete  - Mark a goal complete")
    print("  edit      - Edit a goal's fields")
    print("  delete    - Delete a goal")
    print("  sort      - Show goals sorted by due date (soonest first)")
    print("  filter    - Filter goals by complete/incomplete")
    print("  help      - Show help")
    print("  exit      - Quit")
    print()

def main():
    print("Goal Tracker (PKMS) — Task 3")
    print("Type 'help' for commands.\n")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "add":
            add_goal()
        elif cmd == "list":
            list_goals()
        elif cmd == "search":
            search_goal()
        elif cmd == "complete":
            complete_goal()
        elif cmd == "delete":
            delete_goal()
        elif cmd == "edit":
            edit_goal()
        elif cmd == "sort":
            sort_goals_by_due(ascending=True)
        elif cmd == "filter":
            filter_by_status()
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command (type 'help').\n")

if __name__ == "__main__":
    main()
