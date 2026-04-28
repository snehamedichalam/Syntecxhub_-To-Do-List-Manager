import json
import os

FILE = "tasks.json"
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)
def add_task(tasks):
    title = input("Task title: ").strip()
    tag   = input("Tag (optional, press Enter to skip): ").strip()
    due   = input("Due date (optional, e.g. 2026-05-31): ").strip()
    task  = {
        "title": title,
        "done": False,
        "tag": tag if tag else None,
        "due": due if due else None
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"  ✔ Task '{title}' added.")

def view_tasks(tasks):
    if not tasks:
        print("  No tasks found.")
        return
    print()
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        tag    = f"[{t['tag']}]" if t["tag"] else ""
        due    = f"(due: {t['due']})" if t["due"] else ""
        print(f"  {i}. [{status}] {t['title']} {tag} {due}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"  Deleted: '{removed['title']}'")
    except (ValueError, IndexError):
        print("  Invalid number.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print(f"  Marked done: '{tasks[num-1]['title']}'")
    except (ValueError, IndexError):
        print("  Invalid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Mark task done")
        print("5. Quit")
        choice = input("Choose (1-5): ").strip()

        if   choice == '1': add_task(tasks)
        elif choice == '2': view_tasks(tasks)
        elif choice == '3': delete_task(tasks)
        elif choice == '4': mark_done(tasks)
        elif choice == '5': print("Bye!"); break
        else: print("  Invalid choice.")

main()
