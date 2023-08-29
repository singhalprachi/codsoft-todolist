import uuid  # For generating unique IDs for tasks

# Global variable to store tasks
tasks = []

def add_task(description):
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Task updated successfully!")
            return
    print("Task not found!")

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            status = "✓" if task["completed"] else " "
            print(f"{status} {task['description']}")

def main():
    while True:
        print("\n===== To-Do List App =====")
        print("1. Add Task")
        print("2. Update Task (Mark as Completed)")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            task_id = input("Enter task ID to update: ")
            update_task(task_id)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
