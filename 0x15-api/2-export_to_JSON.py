#!/usr/bin/python3
"""Returns information about an Employee's TODO progress given their id"""
import json
from sys import argv
import requests


if __name__ == '__main__':
    UserId = argv[1]
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={UserId}').json()

    username = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{UserId}').json().get(
            'username')
    with open(f'{UserId}.json', 'wt') as json_file:
        _dict = {f'{UserId}': []}
        for res in response:
            _dict[f'{UserId}'].append(
                {
                    'task': f"{res.get('title')}",
                    'completed': res.get('completed'),
                    'username': f'{username}'
                }
            )
        json.dump(_dict, json_file)
