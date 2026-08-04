import task_manager

def display_menu():
    print("\n" + "=" * 40)
    print("         TASK TRACKER MENU")
    print("=" * 40)
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Completed Tasks")
    print("5. View All To Do Tasks")
    print("6. View All Pending Tasks")
    print("7. Show All Tasks")
    print("8. Exit")
    print("=" * 40)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Add Task selected.")
            task_manager.add_task()

        elif choice == "2":
            print("Edit Task selected.")
            task_manager.update_task()

        elif choice == "3":
            print("Delete Task selected.")
            task_manager.delete_task()

        elif choice == "4":
            print("Show All Completed Tasks.")
            task_manager.mark_completed()

        elif choice == "5":
            print("Show All Incomplete Tasks.")
            task_manager.mark_incomplete()

        elif choice == "6":
            print("Show All Pending Tasks.")
            task_manager.mark_pending_task()

        elif choice == "7":
            print("Show All Tasks.")
            task_manager.all_tasks()

        elif choice == "8":
            print("Thank you for using Task Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()