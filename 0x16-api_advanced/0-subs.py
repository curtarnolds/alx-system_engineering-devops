#!/usr/bin/python3
"""Query the Reddit API and return the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for the given subreddit.
    """
    if type(subreddit) != str:
        return 0
    headers = {'User-Agent': 'MyApi/0.0.1'}
    resp = requests.get('https://www.reddit.com/r/{}/about.json'
                        .format(subreddit),
                        headers=headers, allow_redirects=False)
    if resp.status_code in [302, 404]:
        return 0

    return resp.json().get('data').get('subscribers')
