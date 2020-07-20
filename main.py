import matplotlib
import pandas
import json
import os

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = dict()
users = data.keys()
for user in users:
    for question in data.get(user).get("cases"):
        if question.get("case_id") in questions:
            questions[question.get("case_id")][0] += question.get("final_score")
            questions[question.get("case_id")][1] += len(question.get("upload_records"))
            questions[question.get("case_id")][2] += 1
        else:
            questions[question.get("case_id")] = [question.get("final_score"), len(question.get("upload_records")), 1]

print(questions)
