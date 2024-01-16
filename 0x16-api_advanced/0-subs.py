#!/usr/bin/python3
"""number of subscribers for subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API
    and returns the number of subscribers
    """
    headers = {'User-agent': 'Google Chrome Version 120.0.6099.217'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    try:
        subscribers = response.json().get('data', {}).get('subscribers', 0)
        return subscribers
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return 0
