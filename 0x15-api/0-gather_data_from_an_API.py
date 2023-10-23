#!/usr/bin/python3
"""Retrieve and display to-do list information for a specified employee."""

import requests
import sys


def display_employee_todos(employee_id):
    """
    Retrieve and display to-do list information for a specified employee.

    Args:
        employee_id (int): Employee ID for whom to retrieve to-do information
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(f"{base_url}users/{employee_id}").json()
    todos = requests.get(f"{base_url}todos", params={
                         "userId": employee_id}).json()

    completed_tasks = [task.get("title")
                       for task in todos if task.get("completed")]

    print(f"Employee {user_info.get('name')} has completed \
          {len(completed_tasks)} tasks out of {len(todos)}: ")
    [print(f"\t{task}") for task in completed_tasks]


if __name__ == "__main__":
    display_employee_todos(sys.argv[1])
