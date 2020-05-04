#!/usr/bin/python3
import csv
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
    # file name
    file_name = "{}.csv".format(id)
    # create the file csv
    with open(file_name, "w", newline="") as csvFile:
        field_name = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvFile, field_name, quoting=csv.QUOTE_ALL)
        # writer.writeheader()
        for data in task_data:
            writer.writerow({"USER_ID": id,
                             "USERNAME": user_data.get("username"),
                             "TASK_COMPLETED_STATUS": data.get("completed"),
                             "TASK_TITLE": data.get("title")})
