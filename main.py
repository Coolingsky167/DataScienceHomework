import matplotlib
import pandas
import json
import sklearn

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

        if question.get("case_id") in questions:
            questions[question.get("case_id")][0] += 1
            questions[question.get("case_id")][1] += len(question.get("upload_records"))
            questions[question.get("case_id")][2] += question.get("final_score")
            questions[question.get("case_id")][3] += ACCount
            questions[question.get("case_id")][4] += firstACCount
        else:
            questions[question.get("case_id")] = [
                1,
                len(question.get("upload_records")),
                question.get("final_score"),
                ACCount,
                firstACCount
            ]

print(questions)
print(len(data))
