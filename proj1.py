from datetime import datetime

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!")
        return

    print("\nTo-Do List (sorted by due date):")

    def get_due_date(task):
        if task["due"]:
            return datetime.strptime(task["due"], "%d-%m-%Y")
        else:
            return datetime.max

    sorted_tasks = sorted(tasks, key=get_due_date)

    for i, task in enumerate(sorted_tasks, 1):
        status = "✓" if task["done"] else " "
        due = task["due"] if task["due"] else "No due date"
        warning = ""

        if task["due"] and not task["done"]:
            try:
                due_date = datetime.strptime(task["due"], "%d-%m-%Y").date()
                if due_date < datetime.now().date():
                    warning = " ⚠️ OVERDUE"
            except ValueError:
                warning = " ❓ (Invalid date)"

        print(f"{i}. [{status}] {task['title']} (Due: {due}){warning}")

def add_task():
    title = input("Enter new task: ")
    due = input("Enter due date (DD-MM-YYYY) or leave blank: ")
    tasks.append({"title": title, "done": False, "due": due if due else None})
    print("Task added.")

from datetime import datetime

def update_task():
    show_tasks()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            print(f"Updating: {task['title']} (Current Status: {'Done' if task['done'] else 'Not Done'})")

            # Ask to toggle status
            toggle = input("Toggle status? (y/n): ").lower()
            if toggle == 'y':
                task["done"] = not task["done"]
                print("✔️ Status updated.")
            elif toggle == 'n':
                # Only ask for due date if not toggling status
                change_due = input("Change due date? (y/n): ").lower()
                if change_due == 'y':
                    new_due = input("Enter new due date (DD-MM-YYYY): ")
                    try:
                        due_date = datetime.strptime(new_due, "%d-%m-%Y")
                        task["due"] = due_date.strftime("%d-%m-%Y")
                        print("📅 Due date updated.")
                    except ValueError:
                        print("Invalid date format. Due date not changed.")
                else:
                    print("Skipping due date update.")
            else:
                print("Invalid input. No changes made.")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task (status/due date)")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
