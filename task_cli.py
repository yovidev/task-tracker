import sys, json, os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


def get_timestamp():
    return datetime.now().isoformat()

def find_task(tasks, task_id):
    return next((t for t in tasks if t["id"] == task_id), None)

def add_task(description):
    tasks = load_tasks()
    new_id = max([t['id'] for t in tasks], default=0) + 1
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "created_at": get_timestamp(),
        "updated_at": get_timestamp()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Task not found: {task_id}")
        return
    task["description"] = new_description
    task["updated_at"] = get_timestamp()
    save_tasks(tasks)
    print(f"Task updated successfully (ID: {task_id})")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task not found: {task_id}")
        return
    save_tasks(new_tasks)
    print(f"Task deleted successfully (ID: {task_id})")

def mark_status (task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Task not found: {task_id}")
        return
    task["status"] = status
    task["updated_at"] = get_timestamp()
    save_tasks(tasks)
    print(f"Task marked as {status} (ID: {task_id})")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] ({task['status']}) {task['description']} - Created at: {task['created_at']}, Updated at: {task['updated_at']}")


def main():
    args = sys.argv[1:]
    if not args:
        print("No command provided.")
        return

    command = args[0]
    try:
        if command == "add" and len(args) == 2:
            add_task(args[1])
        elif command == "update" and len(args) == 3:
            update_task(int(args[1]), args[2])
        elif command == "delete" and len(args) == 2:
            delete_task(int(args[1]))
        elif command == "mark-done" and len(args) == 2:
            mark_status(int(args[1]), "done")
        elif command == "mark-in-progress" and len(args) == 2:
            mark_status(int(args[1]), "in-progress")
        elif command == "list":
            if len(args) == 2:
                list_tasks(args[1])
            else:
                list_tasks()
        else:
            print("Invalid command or arguments.")
    except ValueError:
        print("Invalid task ID. It should be an integer.")


if __name__ == "__main__":
    main()




