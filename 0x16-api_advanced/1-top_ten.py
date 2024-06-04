#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a subreddit."""


import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit: The name of the subreddit.

    Prints:
        The titles of the first 10 hot posts or
        None if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, allow_redirects=False).json()
        data = response["data"]["children"]
        for post in data:
            print(post["data"]["title"])

    except Exception:
        print("None")
