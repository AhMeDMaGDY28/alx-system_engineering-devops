#!/usr/bin/python3
"""Queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords."""

    if counts is None:
        counts = {}  # Initialize a dictionary to store word counts

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent
    headers = {"User-Agent": "My Reddit Word Counter Bot"}

    params = {"limit": 100, "after": after}
    try:
        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()
        articles = data["data"]["children"]

        if not articles:
            # No results found for the subreddit
            return counts

        for article in articles:
            title = article["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    # Increment the count for the word
                    counts[word] = counts.get(word, 0) + 1

        # Check if there are more pages (pagination)
        after = data["data"]["after"]
        if after:
            return count_words(
                subreddit, word_list, after=after, counts=counts)
        else:
            # Sort the counts and print the results
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return counts
    except Exception:
        # Invalid subreddit or other error
        return None
