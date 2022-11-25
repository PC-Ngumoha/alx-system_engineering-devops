#!/usr/bin/python3
""" Reads and displays data from an API """
import requests
import sys


if __name__ == '__main__':
    uri = 'https://jsonplaceholder.typicode.com'
    user = requests.get(uri + '/users/{}'.format(sys.argv[1])).json()
    todos = requests.get(uri + '/todos', params={'userId': '{}'
                         .format(sys.argv[1])}).json()

    completed = [todo for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed), len(todos)))
    for task in completed:
        print('\t {}'.format(task.get("title")))
