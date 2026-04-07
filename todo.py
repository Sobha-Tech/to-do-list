tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added!\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n📋 To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✅ Done" if t["done"] else "❌ Not Done"
        print(f"{i}. {t['task']} - {status}")
    print()


def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        print("✅ Task marked as done!\n")
    except:
        print("❌ Invalid input\n")


def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("🗑️ Task deleted!\n")
    except:
        print("❌ Invalid input\n")


def menu():
    while True:
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice\n")


menu()