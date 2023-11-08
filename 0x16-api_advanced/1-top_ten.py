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
    # Define the user agent for the request
    user_agent = "My User Agent 1.0"
    headers = {'User-Agent': user_agent}
    # Construct the API URL for the subreddit and specify a limit of 10 posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Send a GET request to the API and parse the response as JSON
    response = requests.get(url, headers=headers).json()
    # Extract the list of top ten posts from the response
    top_ten_posts = response.get('data', {}).get('children', [])
    if not top_ten_posts:
        return None

    # Print the titles of the top ten posts
    for post in top_ten_posts:
        print(post.get('data', {}).get('title'))
