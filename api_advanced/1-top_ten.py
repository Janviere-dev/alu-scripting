#!/usr/bin/python3
"""
1-top_ten module:
Fetches and prints titles of first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'alu-scripting:v1.0 (by /u/fakebot)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])

    for post in data:
        print(post['data'].get('title'))
