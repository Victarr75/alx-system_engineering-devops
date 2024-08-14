import time
import requests

def recurse(subreddit, hot_list=[], after=None, retry_count=0):
    """
    Recursively queries the Reddit API to return a list of all hot articles' titles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): Accumulates the list of hot article titles.
        after (str): Pagination parameter to fetch the next set of results.
        retry_count (int): Number of retries due to rate limiting.

    Returns:
        list: A list of titles of all hot articles or None if no valid results are found.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        if response.status_code == 429:  # Rate limit reached
            if retry_count < 5:  # Limit number of retries
                wait_time = 2 ** retry_count  # Exponential backoff
                print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                return recurse(subreddit, hot_list, after, retry_count + 1)
            else:
                print("Max retries reached. Exiting.")
                return None

        data = response.json()

        posts = data.get('data', {}).get('children', [])
        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None
    except UnicodeEncodeError as e:
        print(f"Encoding Error: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def save_to_file(hot_list, filename='output.txt'):
    """
    Save the list of hot article titles to a file with UTF-8 encoding.

    Args:
        hot_list (list): List of hot article titles.
        filename (str): Name of the file to save the data.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for title in hot_list:
                f.write(title + '\n')
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Failed to save to file: {e}")

# Example usage
hot_list = recurse('programming')
if hot_list:
    save_to_file(hot_list)
else:
    print("No results to save.")

