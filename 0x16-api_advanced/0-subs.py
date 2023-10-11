#!/usr/bin/python3
"""Query the Reddit API and return the number of subscribers for a given subreddit.
"""
import json
import requests
from sys import argv

# if __name__ == '__main__':


def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for the given subreddit.
    """
    if type(subreddit) != str:
        return 0
    headers = {'User-Agent': 'MyApi/0.0.1'}
    resp = requests.get(
        'https://www.reddit.com/r/{}/top.json'.format(subreddit))
    if resp.status_code == 200:
        return len(resp.json()['data']['children'])
