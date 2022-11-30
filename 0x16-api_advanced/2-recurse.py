#!/usr/bin/python3
"""Returns the total number of subscribers for a particular subreddit or 0"""
import requests


def recurse(subreddit, hot_list=[], counter=0):
    """number_of_subscribers function"""
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(base_url, params={'show': 'all'},
                       headers={'User-Agent': 'Chrome/51.0.2704.103'},
                       allow_redirects=False)
    if res.status_code == 200:
        posts = res.json()
        if counter < len(posts['data']['children']):
            data = posts['data']['children'][counter]
            hot_list.append(data['data']['title'])
            return recurse(subreddit, hot_list, counter + 1)
        elif counter >= len(posts['data']['children']):
            if len(hot_list) == 0:
                return None
            else:
                return hot_list
    else:
        return None
