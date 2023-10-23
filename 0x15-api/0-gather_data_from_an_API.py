#!/usr/bin/python3
"""Retrieve and display a to-do list for a specific employee ID."""
import requests
import sys


def get_employee_todo_list(employee_id):
    base_url, user, todos = "https://jsonplaceholder.typicode.com/",
    requests.get(f"{base_url}users/{employee_id}").json(), requests.get(
        f"{base_url}todos", params={"userId": employee_id}).json()
    completed_tasks, total_tasks = [t["title"]
                                    for t in todos
                                    if t["completed"]], len(todos)
    print(f"Employee {user['name']} is done with tasks
          ({len(completed_tasks)}/{total_tasks}): \n\t" +
          "\n\t".join(completed_tasks))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>") or sys.exit(1)
    get_employee_todo_list(int(sys.argv[1]))
