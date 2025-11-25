#!/usr/bin/python3
"""
Exports all employees' TODO list data to a JSON file.

Format:
{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}
File: todo_all_employees.json
"""

import json
import requests


def fetch_users():
    """Fetch all users from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    return requests.get(url).json()


def fetch_todos():
    """Fetch all TODO tasks from the API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    return requests.get(url).json()


def main():
    """Fetch all tasks and export them to todo_all_employees.json."""
    users = fetch_users()
    todos = fetch_todos()

    data = {}
    user_dict = {u["id"]: u["username"] for u in users}

    for todo in todos:
        uid = todo["userId"]
        if uid not in data:
            data[uid] = []
        data[uid].append({
            "username": user_dict[uid],
            "task": todo["title"],
            "completed": todo["completed"]
        })

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
