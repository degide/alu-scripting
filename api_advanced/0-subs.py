#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}  # avoid Too Many Requests error

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception as e:
        return 0
