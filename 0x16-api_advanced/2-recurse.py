#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recurse it!
    """
    if after is None:
        return []

    headers = {"User-Agent": "wfelipesv"}
    url = "https://www.reddit.com/r/{}".format(subreddit)
    url += "/hot.json?limit=100&after={}".format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)
    # try:
    if (r.status_code != 200):
        return None
    json_data = r.json()
    for item in json_data.get("data").get("children"):
        hot_list.append(item.get("data").get("title"))
    after = json_data.get("data").get("after")
    val_return = recurse(subreddit, [], after)
    return hot_list + val_return
    # except Exception:
    # return None
