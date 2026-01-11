
      
            
  import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. {task['title']} [{status}]")
    print()


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.\n")
        return

    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.\n")


def update_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.\n")
            return

        new_title = input("Enter new task title: ").strip()
        if not new_title:
            print("Task title cannot be empty.\n")
            return

        tasks[index]["title"] = new_title
        save_tasks(tasks)
        print("Task updated successfully.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.\n")
            return

        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def mark_completed(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.\n")
            return

        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
 
         
             
             

     
          
        
                

    


    
  
        
       
        
     
