#!/usr/bin/python3
"""The script queries the Reddit API recursively, parses the titles of
hot articles in a specified subreddit, and prints a sorted count of specified
keywords found in those titles."""

import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    Query the Reddit API recursively, parse the titles of hot articles,
    and print a sorted count of specified keywords.
    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the article titles.
        after (str, optional): A token used to fetch the next page of results.
        word_dict (dict, optional): A dictionary to store the countskeywords.
    Returns:
        None: This function prints the sorted count of keywords.
    """

    # Initialize instances as an empty dictionary if not provided.
    if instances is None:
        instances = {}
    # Define the URL for the Reddit API request.
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    # Set request headers with a user-agent.
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/No-File-2963)"}
    # Define parameters for the API request.
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    # Send a GET request to the Reddit API.
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    try:
        # Try to parse the API response.
        results = response.json()

        # Check for a 404 response (invalid subreddit).
        if response.status_code == 404:
            raise Exception

    except Exception:
        # Handle exceptions (e.g., invalid subreddit or parsing error).
        print("")
        return

    # Extract the relevant data from the API response.
    data = results.get("data")
    after = data.get("after")
    count += data.get("dist")

    # Process each post in the response.
    for c in data.get("children"):
        title = c.get("data").get("title").lower().split()

        # Iterate over the words in the word_list.
        for word in word_list:
            if word.lower() in title:
                times = title.count(word.lower())

                if word not in instances:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if not instances:
            print("")
            return

        # Sort and print the word counts.
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print(f"{k}: {v}")

    else:
        # Continue to the next page of results.
        count_words(subreddit, word_list, instances, after, count)
