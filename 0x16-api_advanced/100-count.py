import requests
import re
from collections import Counter
import time

def recurse(subreddit, word_list, after=None, word_count=None, retry_count=0):
    """
    Recursively queries Reddit API and counts occurrences of keywords in the hot posts titles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Pagination parameter to fetch the next set of results.
        word_count (Counter): Counter object to store word counts.
        retry_count (int): Number of retries for handling rate limiting.

    Returns:
        Counter: Updated Counter object with counts of keywords.
    """
    if word_count is None:
        word_count = Counter()

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        if response.status_code == 429:
            if retry_count < 5:
                wait_time = 2 ** retry_count
                print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                return recurse(subreddit, word_list, after, word_count, retry_count + 1)
            else:
                print("Max retries reached. Exiting.")
                return word_count

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            return word_count

        titles = [post.get('data', {}).get('title', '').lower() for post in posts]
        for title in titles:
            for word in word_list:
                pattern = rf'\b{re.escape(word.lower())}\b'
                word_count[word] += len(re.findall(pattern, title))

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, word_list, after, word_count)
        else:
            return word_count

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return word_count
    except UnicodeEncodeError as e:
        print(f"Encoding Error: {e}")
        return word_count
    except Exception as e:
        print(f"Exception: {e}")
        return word_count

def count_words(subreddit, word_list):
    """
    Counts occurrences of each keyword in the titles of hot posts from a subreddit and prints results.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.

    Returns:
        None
    """
    word_list = [word.lower() for word in word_list]
    word_count = recurse(subreddit, word_list)
    if not word_count:
        return

    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

