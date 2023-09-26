#!/usr/bin/python3
"""Returns information about an Employee's TODO progress given their id"""
import json
import requests


if __name__ == '__main__':
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    with open('todo_all_employees.json', 'wt') as json_file:
        _dict = {}
        for user in users:
            id = user["id"]
            response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={id}'
            ).json()
            _list = []
            for res in response:
                _list.append(
                    {
                        'task': f"{res.get('title')}",
                        'completed': res.get('completed'),
                        'username': f'{user["username"]}'
                    }
                )
            _dict[user['id']] = _list
        json.dump(_dict, json_file)
