import matplotlib
import pandas
import zipfile
import json
import time

import requests

fp = open("sample.json", "r", encoding="UTF-8")
data = json.load(fp)
index = 0
for user in data:
    for test in data.get(user).get("cases"):
        index += 1
print(index)
