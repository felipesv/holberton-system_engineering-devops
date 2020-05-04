#!/usr/bin/python3
import json
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    url += "/users/{}".format(id)
    # bring the user information
    r1 = requests.get(url)
    # bring the tasks information
    url += "/todos".format(id)
    r2 = requests.get(url)
    # get the json data
    user_data = r1.json()
    task_data = r2.json()
    # create dict tasks
    task_list = []
    for data in task_data:
        task_dict = {}
        task_dict["task"] = data.get("title")
        task_dict["completed"] = data.get("completed")
        task_dict["username"] = user_data.get("username")
        task_list.append(task_dict)
    # create the final dict to save
    full_dict = {id: task_list}
    # file name
    file_name = "{}.json".format(id)
    # create the json file
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(full_dict, json_file)
