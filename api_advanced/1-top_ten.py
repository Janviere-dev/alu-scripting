#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit using the Requests library.
If the subreddit is invalid, it prints None.
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
