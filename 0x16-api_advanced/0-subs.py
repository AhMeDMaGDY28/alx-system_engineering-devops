#!/usr/bin/python3
"""this file show the number of the subscriber's"""


import requests


def number_of_subscribers(subreddit):
    api_base_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(api_base_url, allow_redirects=False).json()
        num = response['data']['subscribers']
        return num

    except Exception:
        return 0
