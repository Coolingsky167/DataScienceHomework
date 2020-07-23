import matplotlib
import pandas
import json
import sklearn

import Download
import getQuestions

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = getQuestions.get_questions(data)

