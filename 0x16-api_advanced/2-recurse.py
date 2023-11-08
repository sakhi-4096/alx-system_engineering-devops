#!/usr/bin/python3
"""This script queries the Reddit API to retrieve all hot articles of
a given subreddit."""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles for all hot articles in a given subreddit.
    Returns an empty list if an invalid subreddit is given."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0\
            (by /u/firdaus_cartoon_jr)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    hot_list += [c.get("data").get("title") for c in data.get("children")]

    if data.get("after") is not None:
        return recurse(subreddit, hot_list, data.get("after"),
                       count + data.get("dist"))

    return hot_list
