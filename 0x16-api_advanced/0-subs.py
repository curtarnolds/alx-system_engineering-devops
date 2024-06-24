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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/46.0.2490.80'}
    resp = requests.get('https://www.reddit.com/r/{}/about.json'
                        .format(subreddit),
                        headers=headers, allow_redirects=False)
    if resp.status_code in [302, 404, 403]:
        return 0

    return resp.json().get('data').get('subscribers')
