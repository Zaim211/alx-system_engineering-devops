#!/usr/bin/python3
"""number of subscribers for subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "Zaim211"}
    url = "https://www.reddit.com/r/programming/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        res.json().get('data').get('subscribers')
    else:
        return 0
