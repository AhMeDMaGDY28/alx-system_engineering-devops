#!/usr/bin/python3
"""Fetches titles of all hot articles for a given subreddit using recursion.

This script utilizes the Reddit API to retrieve titles of hot articles
from a specified subreddit. It employs a recursive approach to handle
pagination, ensuring all hot articles are collected even if they span
multiple pages.

**Requirements:**
* Python 3 with `requests` library installed (`pip install requests`)
* Access to the Reddit API (no authentication required for most features)

**Usage:**"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Fetches titles of all hot articles for a
    given subreddit using recursion"""

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent
    headers = {"User-Agent": "My Reddit Hot Articles Bot"}

    params = {"limit": 100, "after": after}
    try:
        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()
        articles = data["data"]["children"]

        if not articles:
            return None  # No results found for the subreddit

        for article in articles:
            hot_list.append(article["data"]["title"])

        # Check if there are more pages (pagination)
        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    except Exception:
        return None
