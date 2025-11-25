#!/usr/bin/python3
"""
Exports an employee's TODO list to CSV.
"""

import csv
import requests
import sys


def main():
    """Main logic for exporting data."""
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        return

    emp_id = sys.argv[1]

    # Fetch employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user = requests.get(user_url).json()
    username = user.get("username")

    # Fetch tasks
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    )
    todos = requests.get(todos_url).json()

    # Write to CSV
    filename = f"{emp_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(
            f, quoting=csv.QUOTE_ALL
        )
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
