#!/usr/bin/python3
"""
This script queries the Reddit API to retrieve the number of 
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """
    # construct the API URL for the subreddit and user agent
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = "My User Agent 1.0"
    headers = {'User-Agent': user_agent}

    # send a GET request to the API and parse the response as JSON
    response = requests.get(url, headers=headers).json()
    # extract the number of subscribers from the response
    subscribers = response.get('data', {}).get('subscribers')

    # return the number of subscribers, or 0 if not available
    return subscribers if subscribers is not None else 0
