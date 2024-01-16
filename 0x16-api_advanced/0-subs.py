#!/usr/bin/python3
"""number of subscribers for subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API
    and returns the number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 120.0.6099.217'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        return respnse.json().get('data').get('subscribers')
    except Exception:
        return 0
