#!/usr/bin/python3
"""Returns information about an Employee's TODO progress given their id"""
import csv
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
    with open(f'{UserId}.csv', 'wt') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for res in response:
            row = (
                f'{UserId}',
                f'{username}',
                f"{res.get('completed')}",
                f"{res.get('title')}"
            )
            writer.writerow(row)
