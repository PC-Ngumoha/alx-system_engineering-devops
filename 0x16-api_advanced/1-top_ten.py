#!/usr/bin/python3
"""Returns the total number of subscribers for a particular subreddit or 0"""
import requests


def top_ten(subreddit):
    """number_of_subscribers function"""
    base_url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    res = requests.get(base_url, params={'show': 'all', 'limit': 10},
                       headers={'User-Agent': 'reddit-scrapper'},
                       allow_redirects=False)
    if res.status_code == 200:
        posts = res.json()
        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
