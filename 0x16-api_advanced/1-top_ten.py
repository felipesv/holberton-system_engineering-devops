#!/usr/bin/python3
# Top Ten
import requests


def top_ten(subreddit):
    """
    Top Ten
    """
    head = {"User-Agent": "wfelipesv"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=head)
    try:
        if (r.status_code != 200):
            raise Exception()
        json_data = r.json()
        for item in json_data.get("data").get("children"):
            print(item.get("data").get("title"))
    except Exception:
        print("None")
