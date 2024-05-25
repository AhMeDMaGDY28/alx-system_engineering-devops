#!/usr/bin/python3
"""This script gathers data from an API for a given employee ID
and exports the TODO list to a CSV file.
Usage: python3 script.py <employee_id>
"""
import csv
import requests
from sys import argv

if len(argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    exit(1)

if __name__ == "__main__":
    try:
        id = int(argv[1])
        API_BASE_URL = "https://jsonplaceholder.typicode.com/"
        users = requests.get(API_BASE_URL + f"users/{id}").json()
        todo_list = requests.get(API_BASE_URL + "todos",
                                 params={"userId": id}).json()

        name = users.get('username')

        with open(f"{id}.csv", mode='w', newline="") as csvFile:
            writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)

            for task in todo_list:
                writer.writerow(
                    [id, name, task.get("completed"), task.get("title")])
    except Exception:
        print("fatal error")
