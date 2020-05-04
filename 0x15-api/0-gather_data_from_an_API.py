#!/usr/bin/python3
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
    # count tasks and complete tasks
    number_task = len(task_data)
    number_comp = 0
    for data in task_data:
        if data.get("completed"):
            number_comp += 1
    # create the lines to print
    line_1 = user_data.get("name")
    line_1 += " is done with tasks"
    line_1 += "({}/{}):".format(number_comp, number_task)
    line_2 = ""
    for data in task_data:
        if data.get("completed"):
            line_2 += "\t "
            line_2 += data.get("title")
            line_2 += "\n"
    # print the lines
    print(line_1)
    print(line_2, end="")
