#!/usr/bin/python3
"""Returns information about an Employee's TODO progress given their id"""
import json
from sys import argv
from urllib import request


UserId = argv[1]
response = json.loads(request.urlopen(
    f'https://jsonplaceholder.typicode.com/todos?userId={UserId}').read()
    .decode('utf-8'))

emp_name = json.loads(request.urlopen(
    f'https://jsonplaceholder.typicode.com/users/{UserId}').read()
    .decode('utf-8')).get('name')
done_tasks = len([comp for comp in response if comp.get('completed') is True])
total_tasks = len(response)


print(
    f"Employee {emp_name} is done with tasks({done_tasks}/{total_tasks}):"
)
for res in response:
    print('\t', res.get('title'))
