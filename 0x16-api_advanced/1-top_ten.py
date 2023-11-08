#!/usr/bin/python3
"""
This script queries the Reddit API to retrieve the titles of the top ten
posts of a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Returns the top ten titles for a given subreddit.
    If the subreddit is invalid, it returns None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/No-File-2963)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
