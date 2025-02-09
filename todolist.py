import os
TASKS_FILE = "tasks.txt"
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def show_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()
def add_task(tasks):
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Task cannot be empty.")
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task")
    except ValueError:
        print("enter a valid number.")
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()