#!/usr/bin/python3
"""
Exports an employee's TODO tasks to a JSON file.
"""

import json
import requests
import sys


def main():
    """Main entry: fetch tasks and export to USER_ID.json"""
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_JSON.py <employee_id>")
        return

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        return

    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    data = {
        str(emp_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = f"{emp_id}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    main()

