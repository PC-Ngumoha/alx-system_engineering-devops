#!/usr/bin/python3
""" Reads and displays data from an API """
import json
import requests
import sys


if __name__ == '__main__':
    uri = 'https://jsonplaceholder.typicode.com'
    users = requests.get(uri + '/users').json()

    with open('todo_all_employees.json', 'w') as file:
        output = {}
        for user in users:
            todos = requests.get(uri + '/todos', params={'userId': '{}'
                                 .format(user.get("id"))}).json()
            user_id = user.get("id")
            username = user.get("username")
            data = []
            for todo in todos:
                data.append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })
            output[user_id] = data
        json.dump(output, file)
