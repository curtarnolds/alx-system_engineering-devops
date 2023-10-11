#!/usr/bin/python3
"""A recursive function that queries the Reddit API and prints
the count of given words
"""
import requests


def count_words(subreddit,  word_list=[], after=None, _dict={}):
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
        title_string = ' '.join([post.get('data').get('title') for post in
                                 resp_json.get('data').get('children')])
        for key in word_list:
            value = title_string.lower().count(key.lower())
            _dict[key] = value + _dict.get(key, 0)
        if after:
            count_words(subreddit, word_list=word_list,
                        after=after, _dict=_dict)
        else:
            sorted_dict = dict(
                sorted(_dict.items(), key=lambda key: key[1], reverse=True))
            for k, v in sorted_dict.items():
                if v > 0:
                    print(f'{k}: {v}')
            return sorted_dict
    except requests.JSONDecodeError:
        return
