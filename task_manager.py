import datetime
import json
import os

# Name of the JSON file where all tasks are stored
Filename = "data.json"


def load_data():
    """
    Loads and returns the list of tasks from the JSON file.
    Returns an empty list if the file doesn't exist yet or is empty,
    so the rest of the program can always assume it's getting a list.
    """
    if not os.path.exists(Filename):
        return []

    with open(Filename, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)


def id_gen(task):
    """
    Generates the next task ID.
    If there are no tasks yet, starts at 1.
    Otherwise, takes the ID of the last task in the list and adds 1.
    """
    if len(task) == 0:
        return 1
    return task[-1]["id"] + 1


def add_task():
    """
    Prompts the user for a new task's details, generates an ID for it,
    appends it to the existing list of tasks, and saves everything
    back to the JSON file.
    """
    status = ""

    title = input("Enter your task's title: ")
    description = input("Enter your task's description: ")

    print("\n Please select the task status: ")
    print("1. Pending")
    print("2. Completed")
    print("3. To Do")
    choice = input("Enter your choice: ")

    if choice == "1":
        status = "Pending"
    elif choice == "2":
        status = "Completed"
    elif choice == "3":
        status = "To Do"
    else:
        print("Invalid choice. Please try again.")

    # Load existing tasks first, so we don't overwrite them
    task = load_data()

    # Build the new task as a dictionary
    data = {
        "id": id_gen(task),
        "title": title,
        "description": description,
        "status": status,
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }

    # Add the new task to the list, then save the whole list back to file
    task.append(data)

    with open(Filename, "w") as f:
        json.dump(task, f, indent=4)

    print(f"Task '{title}' added to database.")


def update_task():
    """
    Lets the user pick an existing task by ID and edit its title,
    description, or status. Updates the "updatedAt" timestamp
    whenever a change is actually made.
    """
    task = load_data()

    task_id = input("\nPlease type the task id to update: ")

    # Tracks whether we found a matching task, so we only print
    # "There's no task with that ID" once, and only if nothing matched
    found = False

    for t in task:
        if t["id"] == int(task_id):
            found = True
            print(f"Current task title: {t['title']} selected.")
            print("What would you like to edit?")
            print("1. Title")
            print("2. Description")
            print("3. Status")
            print("4. Cancel")
            choice = input("Enter your choice: ")

            if choice == "1":
                t["title"] = input("Enter new title: ")
                t["updatedAt"] = datetime.datetime.now().isoformat()
                print("New title has been updated.")
            elif choice == "2":
                t["description"] = input("Enter new description: ")
                t["updatedAt"] = datetime.datetime.now().isoformat()
                print("New description has been updated.")
            elif choice == "3":
                print("Please select the task status: ")
                print("1. Pending")
                print("2. Completed")
                print("3. To Do")
                choice = input("\nEnter your choice: ")

                if choice == "1":
                    t["status"] = "Pending"
                    t["updatedAt"] = datetime.datetime.now().isoformat()
                    print(f"{t['title']} Status has been updated.")
                elif choice == "2":
                    t["status"] = "Completed"
                    t["updatedAt"] = datetime.datetime.now().isoformat()
                    print(f"{t['title']} Status has been updated.")
                elif choice == "3":
                    t["status"] = "To Do"
                    t["updatedAt"] = datetime.datetime.now().isoformat()
                    print(f"{t['title']} Status has been updated.")
                else:
                    print("Invalid choice. Please try again.")
            elif choice == "4":
                # User cancelled, so exit the loop without saving
                break
            else:
                print("Invalid choice. Please try again.")

            # Save the full task list back to file (not just this one task)
            with open(Filename, "w") as f:
                json.dump(task, f, indent=4)
            break

    if not found:
        print("There's no task with that ID.")


def delete_task():
    """
    Lets the user pick an existing task by ID, confirms with them,
    then removes it from the list and saves the updated list to file.
    """
    task = load_data()

    task_id = input("\nPlease type the task id to delete: ")

    found = False

    for t in task:
        if t["id"] == int(task_id):
            found = True
            print(f"Current task title: {t['title']} selected.")
            choice = input(f"Are you sure you want to delete this task called {t['title']}? (y/n)\n")

            if choice == "y":
                # Remove this specific task from the list
                task.remove(t)

                with open(Filename, "w") as f:
                    json.dump(task, f, indent=4)

                print(f"Task '{t['title']}' deleted.")
            elif choice == "n":
                print("Delete cancelled.")
            else:
                print("Invalid choice. Please try again.")
            break

    if not found:
        print("There's no task with that ID.")


def mark_completed():
    """
    Displays all tasks whose status is "Completed" in a readable format.
    """
    tasks = load_data()
    completed = [t for t in tasks if t["status"] == "Completed"]

    if not completed:
        print("\nNo completed tasks found.")
        return

    print("\n" + "=" * 40)
    print("       COMPLETED TASKS")
    print("=" * 40)

    for t in completed:
        print(f"\nID:          {t['id']}")
        print(f"Title:       {t['title']}")
        print(f"Description: {t['description']}")
        print(f"Created:     {t['createdAt']}")
        print(f"Updated:     {t['updatedAt']}")
        print("-" * 40)


def mark_incomplete():
    """
    Displays all tasks whose status is "To Do" in a readable format.
    """
    tasks = load_data()
    incomplete = [t for t in tasks if t["status"] == "To Do"]

    if not incomplete:
        print("\nNo To Do tasks found.")
        return

    print("\n" + "=" * 40)
    print("       To Do TASKS")
    print("=" * 40)

    for t in incomplete:
        print(f"\nID:          {t['id']}")
        print(f"Title:       {t['title']}")
        print(f"Description: {t['description']}")
        print(f"Created:     {t['createdAt']}")
        print(f"Updated:     {t['updatedAt']}")
        print("-" * 40)


def mark_pending_task():
    """
    Displays all tasks whose status is "Pending" in a readable format.
    """
    tasks = load_data()
    pending = [t for t in tasks if t["status"] == "Pending"]

    if not pending:
        print("\nNo Pending tasks found.")
        return

    print("\n" + "=" * 40)
    print("       To Do TASKS")
    print("=" * 40)

    for t in pending:
        print(f"\nID:          {t['id']}")
        print(f"Title:       {t['title']}")
        print(f"Description: {t['description']}")
        print(f"Created:     {t['createdAt']}")
        print(f"Updated:     {t['updatedAt']}")
        print("-" * 40)


def all_tasks():
    """
    Displays every task currently saved, regardless of status.
    """
    tasks = load_data()

    for t in tasks:
        print(f"\nID:          {t['id']}")
        print(f"Title:       {t['title']}")
        print(f"Description: {t['description']}")
        print(f"Status:      {t['status']}")
        print(f"Created:     {t['createdAt']}")
        print(f"Updated:     {t['updatedAt']}")
        print("-" * 40)
