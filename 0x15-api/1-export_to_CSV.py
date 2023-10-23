#!/usr/bin/python3
"""Export to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


def export_to_csv(user_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + f"users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, t.get(
            "completed"), t.get("title")]) for t in todos]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(user_id)
