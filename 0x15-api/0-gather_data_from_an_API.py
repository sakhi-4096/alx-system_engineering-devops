#!/usr/bin/python3
"""Retrieve and display to-do list information for a specified employee."""

import requests
import sys


def display_employee_todos():
    """
    Retrieve and display to-do list information for a specified employee.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(f"{base_url}users/{sys.argv[1]}").json()
    todos = requests.get(f"{base_url}todos", params={
                         "userId": sys.argv[1]}).json()

    completed_tasks = [task.get("title")
                       for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user_info.get("name"), len(completed_tasks), len(todos)))
    [print(f"\t {task}") for task in completed_tasks]


if __name__ == "__main__":
    display_employee_todos()
