#!/usr/bin/python3
"""Returns the total number of subscribers for a particular subreddit or 0"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers function"""
    base_url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    res = requests.get(base_url, params={'show': 'all'},
                       headers={'User-Agent': 'Chrome/51.0.2704.103'},
                       allow_redirects=False)
    if res.status_code == 200:
        output = res.json()
        data = output['data']['children'][0]
        return data['data']['subreddit_subscribers']
    else:
        return 0
