#!/usr/bin/python3
import requests
import sys
import json

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    # bring the user information
    r1 = requests.get(url)
    data_users = r1.json()
    # create data for each user
    full_dict = {}
    for user in data_users:
        # bring the task information
        url2 = "{}/{}/todos".format(url, user.get("id"))
        r2 = requests.get(url2)
        data_task = r2.json()
        # create dict with each task
        task_list = []
        for data in data_task:
            task_dict = {}
            task_dict["username"] = user.get("username")
            task_dict["task"] = data.get("title")
            task_dict["completed"] = data.get("completed")
            task_list.append(task_dict)
        # create the final dict to save
        full_dict[user.get("id")] = task_list

    # create the json file
    file_name = "todo_all_employees.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(full_dict, json_file)
