#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles
of the first 10 hot posts from a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'alu-scripting:v1.0 (by /u/fakebot)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
