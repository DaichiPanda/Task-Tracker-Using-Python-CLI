[README.md](https://github.com/user-attachments/files/30709365/README.md)

# Task Tracker

A simple command-line task tracker built in Python. Add, edit, delete, and view tasks — all saved locally to a JSON file, so your data persists between runs.

Task Tacker Link: https://github.com/DaichiPanda/Task-Tracker-Using-Python-CLI/tree/master

## Features

- **Add Task** — create a new task with a title, description, and status
- **Edit Task** — update a task's title, description, or status by ID
- **Delete Task** — remove a task by ID (with confirmation)
- **View by Status** — list all tasks that are Completed, Pending, or To Do
- **View All Tasks** — see every task currently saved
- Automatic timestamps (`createdAt` / `updatedAt`) tracked for every task
- Data is stored in a local `data.json` file — no database setup required

## Project Structure

```
.
├── task_tracker_menu.py   # Entry point — displays the menu and handles user input
├── task_manager.py        # Core logic — add/update/delete/view tasks, JSON storage
└── data.json               # Auto-created on first run — stores all task data
```

## Requirements

- Python 3.7 or higher (no external packages needed — uses only the standard library)

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/task-tracker.git
   cd task-tracker
   ```

2. Run the program:
   ```bash
   python task_tracker_menu.py
   ```

3. Follow the on-screen menu to add, edit, delete, or view tasks.

## Usage

When you run the program, you'll see a menu like this:

```
========================================
         TASK TRACKER MENU
========================================
1. Add Task
2. Edit Task
3. Delete Task
4. Update Status Task
5. View All Completed Tasks
6. View All Incomplete Tasks
7. View All in Progress Tasks
8. Exit
========================================
```

Enter the number corresponding to the action you want, then follow the prompts.

### Example: Adding a task

```
Enter your task's title: Buy groceries
Enter your task's description: Milk, eggs, bread

Please select the task status:
1. Pending
2. Completed
3. To Do
Enter your choice: 1

Task 'Buy groceries' added to database.
```

Each task is saved with a unique auto-incrementing ID, so you can reference it later when editing or deleting.

## Data Storage

All tasks are stored in `data.json` in the following format:

```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "status": "Pending",
        "createdAt": "2026-08-04T10:23:11.123456",
        "updatedAt": "2026-08-04T10:23:11.123456"
    }
]
```

This file is created automatically the first time you add a task — you don't need to create it manually.

## Roadmap / Ideas for Improvement

- [ ] Search tasks by title or keyword
- [ ] Sort tasks by date or status
- [ ] Add due dates and reminders
- [ ] Export tasks to CSV
- [ ] Add unit tests

## License

This project is open source and available for personal or educational use.
