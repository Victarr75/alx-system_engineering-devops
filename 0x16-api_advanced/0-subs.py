#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid rate limiting issues
    headers = {'User-Agent': 'myUserAgent'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # Return 0 if the subreddit is invalid or other error occurs
            return 0
    except requests.RequestException:
        # Return 0 if there is a network-related error
        return 0

