#!/usr/bin/python3
""" Reads and displays data from an API """
import csv
import requests
import sys


if __name__ == '__main__':
    uri = 'https://jsonplaceholder.typicode.com'
    user = requests.get(uri + '/users/{}'.format(sys.argv[1])).json()
    todos = requests.get(uri + '/todos', params={'userId': '{}'
                         .format(sys.argv[1])}).json()

    with open('{}.csv'.format(user.get("id")), 'w') as file:
        writer = csv.writer(file)
        user_id, username = (user.get("id"), user.get("username"))
        for todo in todos:
            status, title = (todo.get("completed"), todo.get("title"))
            writer.writerow([user_id, username, status, title])
