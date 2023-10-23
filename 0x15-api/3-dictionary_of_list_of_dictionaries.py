#!/usr/bin/python3
"""Export to-do list information of all employees to JSON format."""
import json
import requests


def export_all_to_json():
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{base_url}users").json()

    data = {
        u.get("id"): [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username"),
            } for t in (requests.get(f"{base_url}todos",
                                     params={"userId": u.get("id")}).json())
        ] for u in users
    }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
