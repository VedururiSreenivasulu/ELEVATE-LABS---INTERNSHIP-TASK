
FILENAME="tasks.txt"
def load_tasks():
    try:
        with open(FILENAME,"r") as file:
            tasks=[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task+"\n")
def add_task():
    task=input("Enter a task to add: ").strip()
    if task:
        tasks=load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print(" Cannot add an empty task.")

def view_tasks():
    tasks=load_tasks()
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks found.")

def remove_task():
    tasks=load_tasks()
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks()
    try:
        number=int(input("Enter task number to remove: "))
        if 1<=number<=len(tasks):
            removed=tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1.View Tasks")
        print("2.Add Task")
        print("3.Remove Task")
        print("4.Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice=="1":
            view_tasks()
        elif choice=="2":
            add_task()
        elif choice=="3":
            remove_task()
        elif choice=="4":
            print("Exiting.Goodbye!")
            break
        else:
            print("Invalid choice.Please choose 1 to 4.")
if __name__=="__main__":
    main()
