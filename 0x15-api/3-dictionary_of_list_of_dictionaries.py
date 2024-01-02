#!/usr/bin/python3
""" Dictionary of list of diectionaries """
import requests
from sys import argv
import json


def list_dictionaries():
    """ List of tasks for all employees """
    api_url = 'https://jsonplaceholder.typicode.com/'
    users_url = f'{api_url}/users/'

    users_list = requests.get(users_url).json()

    with open(f'todo_all_employees.json', mode='w', encoding='utf-8') as file:
        json.dump({user.get('id'): [
            {
                'usename': user.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed')
            }
            for task in requests.get('{}/{}/todos/'
                                     .format(users_url, user.get('id'))).json()
        ] for user in users_list}, file)


if __name__ == "__main__":
    list_dictionaries()
