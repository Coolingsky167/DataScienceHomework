import json


def get_questions(data):
    questions = dict()
    users = data.keys()
    for user in users:
        for question in data[user]['cases']:
            ACCount = 0
            firstACCount = 0
            upload_records = question.get("upload_records")
            totalScore = sum(x['score'] for x in upload_records)
            uploadTimes = len(upload_records)
            debugEffect = 0
            debugTimes = 0
            if uploadTimes > 1:
                debugEffect = (question.get('final_score') - upload_records[0].get("score")) * 60 * 1000 / \
                              (upload_records[uploadTimes - 1].get("upload_time") - upload_records[0].get(
                                  "upload_time"))
                debugTimes = 1
            if question.get("final_score") == 100:
                ACCount = 1
            if ((uploadTimes > 0) and (upload_records[0].get("score") == 100.0)) \
                    or (uploadTimes == 0 and ACCount == 1):
                firstACCount = 1

            if question.get("case_id") in questions:
                questions[question.get("case_id")][0] += 1
                questions[question.get("case_id")][1] += len(question.get("upload_records"))
                questions[question.get("case_id")][2] += question.get("final_score")
                questions[question.get("case_id")][3] += ACCount
                questions[question.get("case_id")][4] += firstACCount
                questions[question.get("case_id")][5] += totalScore
                questions[question.get("case_id")][6] += debugTimes
                questions[question.get("case_id")][7] += debugEffect
            else:
                questions[question.get("case_id")] = [
                    1,
                    uploadTimes,
                    question.get("final_score"),
                    ACCount,
                    firstACCount,
                    totalScore,
                    debugTimes,
                    debugEffect
                ]

    for key in questions.keys():
        try:
            temp = questions[key]
            questions[key] = [
                temp[3] / temp[0] * 100,  # AC率
                temp[4] / temp[0] * 100,  # 1A率
                100 / temp[1],  # 1 / 提交次数
                temp[2] / temp[0],  # 最终得分的平均分
                temp[5] / temp[1],  # 每次提交的平均分
                temp[7] / temp[6]  # 平均每个人的debug成效
            ]
        except ZeroDivisionError:
            print(key)
            print(questions[key])
    return questions


if __name__ == '__main__':
    fp = open("sample.json", "r", encoding="UTF-8")
    data = json.load(fp)
    print(get_questions(data))