#!/usr/bin/python3
""" Query the Reddit API and prints the titles of the first 10 hot posts """

import requests


def top_ten(subreddit):
    """ Return top 10 hot posts titles """
    api_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "User-Agent": "Mira top"
    }
    params = {
        "limit": 10
    }
    response = requests.get(api_url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        print('None')

    data = response.json()['data']['children']
    for post in data:
        print(post['data']['title'])
