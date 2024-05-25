#!/usr/bin/python3
"""This script gathers data from an API for a given employee ID
and exports the TODO list to a CSV file.
Usage: python3 script.py <employee_id>
"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    try:
        id = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url + f"user/{id}").json()
        username = user.get("username")
        todo = requests.get(url + "todos", params={"userId": id}).json()
        data = {
            id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todo
            ]}
        json_data = json.dumps(data, indent=4)
        with open(f"{id}.json", mode="w", newline='') as json_file:
            json_file.write(json_data)

    except Exception:
        print("error in the body")
