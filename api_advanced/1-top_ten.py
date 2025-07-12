#!/usr/bin/python3
"""Get titles of top 10 hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:top.ten:v1.0 (by /u/alumunezero)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        titles = [post["data"]["title"] for post in posts]

        for title in titles:
            print(title)
    except requests.RequestException:
        print(None)
