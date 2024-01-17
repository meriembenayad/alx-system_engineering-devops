#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
from sys import argv
import requests


def number_of_subscribers(subreddit):
    """ Return number of subscriber """
    headers = {"User-Agent": "unique-user-agent"}
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if (response.status_code == 200):
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
