import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["done"] else "✖ Pending"
        print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        tasks[index]["title"] = input("Enter new task title: ")
        save_tasks(tasks)
        print("Task updated.")
    except:
        print("Invalid input.")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except:
        print("Invalid input.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
