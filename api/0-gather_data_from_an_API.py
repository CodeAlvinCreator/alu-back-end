#!/usr/bin/env python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user info
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    # Completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    # Print progress
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))

    # Print completed task titles
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
