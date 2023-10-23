#!/usr/bin/python3
"""Export to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def export_to_json(user_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + f"users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.json", "w") as jsonfile:
        data = {
            user_id: [
                {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": username,
                } for t in todos
            ]
        }
        json.dump(data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_json(user_id)
