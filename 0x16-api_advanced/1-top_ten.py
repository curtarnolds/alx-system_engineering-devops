#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import json
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed"""
    if type(subreddit) != str:
        print('None')

    headers = {'User-Agent': 'MyApi/0.0.1'}
    payload = {'limit': 10}
    resp = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                        headers=headers, params=payload,
                        allow_redirects=False)
    if resp.status_code in [302, 404]:
        print('None')
    try:
        resp_json = resp.json()
        for post in resp_json.get('data').get('children'):
            print(post.get('data').get('title'))
    except requests.JSONDecodeError:
        print('None')
