# the start display menu for the tdl

def display_menu():
    print("   To Do List")
    print("     Menu:")
    print("1. Add a Task (+)")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

# to add a task on the tdl

def add_task(tasks):
    task = input("Enter a Task: ")
    tasks.append(task)
    print("Task Added")

# to view the task on the tdl
# line 23, 24 is to keep track of the loops that has done

def view_tasks(tasks):
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
# if there isn't a task to mark as done it will show a messege
# if there is a task it will mark it as done and remove it from the list

def task_done(tasks):
    if not tasks:
        print("Error 404 Not Found")
        return

    view_tasks(tasks)
    index = int(input("Enter task index to mark as done: ")) - 1

    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}'was marked as done and was removed.")
    else:
        print("Wrong task index.")

# the loop for the choices

def main():
    tasks = []

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_done(tasks)
        elif choice == '4':
            print("Closing To Do List")
            break
        else:
            print("Wrong choice. Select 1, 2 or 3.")

if __name__ == "__main__":
    main()