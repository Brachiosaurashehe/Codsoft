import os

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from the text file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    """Save the current list of tasks to the text file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    while True:
        tasks = load_tasks()
        print(f"\n--- TO-DO LIST ({len(tasks)} tasks) ---")
        
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
        print("\nOptions: [1] Add Task  [2] Remove Task  [3] Exit")
        choice = input("Select an option: ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            if new_task.strip():
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added!")
        
        elif choice == "2":
            if not tasks:
                print("Nothing to delete.")
                continue
            try:
                idx = int(input("Enter the task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()

     
          
        
                

    


    
  
        
       
        
     
