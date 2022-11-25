#!/usr/bin/python3
""" Reads and displays data from an API """
import json
import requests
import sys


if __name__ == '__main__':
    uri = 'https://jsonplaceholder.typicode.com'
    user = requests.get(uri + '/users/{}'.format(sys.argv[1])).json()
    todos = requests.get(uri + '/todos', params={'userId': '{}'
                         .format(sys.argv[1])}).json()

    user_id = user.get("id")
    username = user.get("username")
    with open('{}.json'.format(user_id), 'w') as file:
        data = []
        for todo in todos:
            data.append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            })
        json.dump({user_id: data}, file)
