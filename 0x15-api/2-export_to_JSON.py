#!/usr/bin/python3
"""Returns information about an Employee's TODO progress given their id"""
import json
from sys import argv
from urllib import request


if __name__ == '__main__':
    UserId = argv[1]
    response = json.loads(request.urlopen(
        f'https://jsonplaceholder.typicode.com/todos?userId={UserId}').read()
        .decode('utf-8'))

    username = json.loads(request.urlopen(
        f'https://jsonplaceholder.typicode.com/users/{UserId}').read()
        .decode('utf-8')).get('username')
    with open(f'{UserId}.json', 'wt') as json_file:
        _dict = {f'{UserId}': []}
        for res in response:
            _dict[f'{UserId}'].append(
                {
                    'task': f"{res.get('title').lower()}",
                    'completed': f"{res.get('completed').lower()}",
                    'username': f'{username}'
                }
            )
        json.dump(_dict, json_file)
