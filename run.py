#! /usr/bin/env python3

import os
import requests

# feedback_dir = "/data/feedback/"
# feedback_dir_lst = os.listdir("/data/feedback/")
feedback_dir = "./feedback/"
feedback_dir_lst = os.listdir("./feedback/")
for file in feedback_dir_lst:
    dict1 = {}
    x = 0
    column = ["title", "name", "date", "feedback"]
    with open(feedback_dir + file) as txt_file:
        for line in txt_file:
            dict1[column[x]] = line.strip()
            x += 1
        print(dict1)
    response = requests.post("http://104.197.81.83/feedback/", json=dict1)
print(response.request.body)
print(response.status_code)
