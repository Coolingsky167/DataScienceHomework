import matplotlib
import pandas
import numpy as np
import json
from sklearn.decomposition import PCA

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = dict()
users = data.keys()
for user in users:
    for question in data.get(user).get("cases"):
        ACCount = 0
        firstACCount = 0
        if question.get("final_score") == 100:
            ACCount = 1
        if (len(question.get("upload_records")) > 1) and (question.get("upload_records")[0].get("score") == 100.0):
            firstACCount = 1

        scoreSum = sum([x.get("score") for x in question.get("upload_records")])

        if question.get("case_id") in questions:
            questions[question.get("case_id")][0] += 1
            questions[question.get("case_id")][1] += len(question.get("upload_records"))
            questions[question.get("case_id")][2] += question.get("final_score")
            questions[question.get("case_id")][3] += scoreSum
            questions[question.get("case_id")][4] += ACCount
            questions[question.get("case_id")][5] += firstACCount
        else:
            questions[question.get("case_id")] = [
                1,
                len(question.get("upload_records")),
                question.get("final_score"),
                scoreSum,
                ACCount,
                firstACCount
            ]

for key in questions:
    questions[key][2] = questions[key][2] / questions[key][0]
    questions[key][3] = questions[key][3] / questions[key][1]
    questions[key][4] = questions[key][4] / questions[key][0]
    questions[key][5] = questions[key][5] / questions[key][0]
    print(questions[key])

print(len(data))
