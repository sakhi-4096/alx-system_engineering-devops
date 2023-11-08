#!/usr/bin/python3
"""The script queries the Reddit API recursively, parses the titles of
hot articles in a specified subreddit, and prints a sorted count of specified
keywords found in those titles."""

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
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
        word_dict = {}

    if after is None:
        word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in word_dict:
            if count:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'RedditKeywordCounter:v1.0 (by /u/No-File-2963)'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header,
                            params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()['data']
        children = data['children']
        aft = data['after']
        for post in children:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_list:
                word_dict[word] = word_dict.get(
                    word, 0) + lower.count(word.lower())

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
