#!/usr/bin/python3
""" Query the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ Return number of subscriber """
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "windows:0x16.api.advanced:v1.0.0 (by /u/mira)"
    }
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    if (response.status_code == 200):
        data = response.json()
        return data['data']['subscribers']
    return 0
