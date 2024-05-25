from sys import argv, exit
import requests

#!/usr/bin/python3
"""hello"""


if len(argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    exit(1)

if __name__ == "__main__":
    employee_id = int(argv[1])

    try:
        # employee data
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_data = requests.get(employee_url).json()
        employee_name = employee_data.get('name')

        # the data of to do list
        to_do_list_url = f"https://jsonplaceholder.typicode.com/todos"
        to_do_list_data = requests.get(to_do_list_url, params={
                                       "userId": employee_id}).json()

        total_tasks = len(to_do_list_data)
        done_tasks = [task.get("title")
                      for task in to_do_list_data if task.get('completed')]
        num_done_tasks = len(done_tasks)

        print(
            f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")

        for task in to_do_list_data:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
