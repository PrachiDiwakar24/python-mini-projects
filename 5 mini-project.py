tasks = []

while True:

    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Removed:", removed)

            else:
                print("Invalid task number.")

    elif choice == "4":
        
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")