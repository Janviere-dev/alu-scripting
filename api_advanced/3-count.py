#!/usr/bin/python3
"""
Module that recursively queries Reddit API for hot posts and counts keyword appearances.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively fetches titles from hot posts in a subreddit and counts given keywords.
    """
    headers = {'User-Agent': 'alu-scripting:v1.0 (by /u/fakebot)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    posts = response.json().get('data', {}).get('children', [])
    after = response.json().get('data', {}).get('after')

    # Normalize keywords to lowercase, combine duplicates
    normalized = [word.lower() for word in word_list]
    keyword_set = set(normalized)
    for post in posts:
        title = post.get('data', {}).get('title', '').lower().split()
        for key in keyword_set:
            count = title.count(key)
            if count > 0:
                word_count[key] = word_count.get(key, 0) + count

    if after:
        return count_words(subreddit, word_list, after, word_count)

    # Print final result
    sorted_items = sorted(
        [(k, v) for k, v in word_count.items() if v > 0],
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_items:
        print(f"{word}: {count}")

