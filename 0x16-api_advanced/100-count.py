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

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/No-File-2963)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
