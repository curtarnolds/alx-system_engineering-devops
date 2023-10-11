#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
 are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hotlist=[], after=None):
    """Return a list containing the titles of all hot articles for a given
    subreddit
    """
    if type(subreddit) != str:
        return

    headers = {'User-Agent': 'MyApi/0.0.1'}
    payload = {
        'limit': 50,
        'after': after
    }
    resp = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                        headers=headers, params=payload,
                        allow_redirects=False)
    if resp.status_code in [302, 404]:
        return

    try:
        resp_json = resp.json()
        after = resp_json.get('data').get('after')
        for post in resp_json.get('data').get('children'):
            hotlist.append(post.get('data').get('title'))
        if after:
            recurse(subreddit=subreddit, hotlist=hotlist, after=after)
    except requests.JSONDecodeError:
        return
    return hotlist
