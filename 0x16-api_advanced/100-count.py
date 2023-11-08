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

    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_dict = sorted(
            word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count:
                print(f"{word}: {count}")
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')

    for post in children:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_dict:
            word_dict[word] += title.count(word)

    count_words(subreddit, word_list, after, word_dict)
