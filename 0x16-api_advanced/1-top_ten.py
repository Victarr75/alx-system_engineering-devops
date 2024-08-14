#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    except Exception as e:
        print(None)
