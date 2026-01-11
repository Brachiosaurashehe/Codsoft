
def load_tasks():
    if not hasattr(load_tasks, "_init"): # Check if file exists
        open(FILENAME, "a").close() 
    with open(FILENAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    while True:
        tasks = load_tasks()
        print(f"\n--- TO-DO LIST ({len(tasks)} tasks) ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        
        print("\nOptions: [1] Add  [2] Remove  [3] Exit")
        choice = input("Select: ")

        if choice == "1":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
        elif choice == "2":
            idx = int(input("Enter number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

    


    
  
        
       
        
     
