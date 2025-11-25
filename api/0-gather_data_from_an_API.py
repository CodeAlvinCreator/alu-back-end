#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This module retrieves TODO list progress for a given employee ID
from the JSONPlaceholder REST API.

It fetches:
- The employee's name
- All tasks assigned to the employee
- Tasks that are completed

It then prints the progress in the required format:
Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
    TASK_TITLE  (for each completed task)

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    # Count completed vs total
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    # Print the required first line
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))

    # Print completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
