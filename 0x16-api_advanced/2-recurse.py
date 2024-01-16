#!/usr/bin/python3
"""
list containing the titles of all hot articles for a given subreddit.
"""
from requests import get


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    recursive function that queries the Reddit API and returns 
    a list containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Zaim211"}
    params = {
        "after": after,
        "limit": 1
    }
    response = get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        hot_post = data['children'][0]
        hot_list.append(hot_post['data']['title'])
        if len(data['children']) > 1:
            hot_post = data['children'][1]
            hot_list.append(hot_post['data']['title'])
        if data['after']:
            return recurse(subreddit, hot_list=hot_list, after=data['after'])
        else:
            return hot_list
    else:
        return None
