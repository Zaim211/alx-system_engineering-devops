#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Zaim211'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()['data']['children']
        for post in results:
            print(post['data']['title'])
    else:
        print(None)
