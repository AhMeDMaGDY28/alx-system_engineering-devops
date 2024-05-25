#!/usr/bin/python3
"""This script gathers data from an API for a given employee ID.
The script takes an employee ID as a command-line argument and makes
API requests to retrieve the employee's data and their to-do list.
It then prints out the employee's name, the number of completed tasks,
and the list of completed tasks.
Usage: python3 script.py <employee_id>
"""
import requests
from sys import argv, exit


if len(argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    exit(1)

    # Make API requests and process the data here
if __name__ == "__main__":
    employee_id = int(argv[1])
    API_BASE_URL = "https://jsonplaceholder.typicode.com/"
    try:
        # employee data
        employee_url = API_BASE_URL + f"users/{employee_id}"
        employee_data = requests.get(employee_url).json()
        employee_name = employee_data.get('name')

        # the data of to do list
        to_do_list_url = API_BASE_URL + f"todos"
        to_do_list_data = requests.get(to_do_list_url, params={
                                       "userId": employee_id}).json()

        total_tasks = len(to_do_list_data)
        done_tasks = [task.get("title")
                      for task in to_do_list_data if task.get('completed')]
        num_done_tasks = len(done_tasks)

        print(
            f"Employee {employee_name}" +
            f" is done with tasks({num_done_tasks}/{total_tasks}):"
        )

        for task in done_tasks:
            print(f"\t {task}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
