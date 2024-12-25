def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add? "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            if not tasks:
                print("\nNo tasks available.")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            if not tasks:
                print("\nNo tasks available to update.")
            else:
                task_index = int(input("Enter the task number to update: ")) - 1
                if 0 <= task_index < len(tasks):
                    updated_task = input("Enter the updated task: ")
                    tasks[task_index]["task"] = updated_task
                    print("Task updated!")
                else:
                    print("Invalid task number.")

        elif choice == '4':
            if not tasks:
                print("\nNo tasks available to mark as done.")
            else:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")

        elif choice == '5':
            if not tasks:
                print("\nNo tasks available to delete.")
            else:
                task_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Task '{removed_task['task']}' deleted!")
                else:
                    print("Invalid task number.")

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
