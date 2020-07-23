import matplotlib
import pandas
import numpy as np
import json
from sklearn.decomposition import PCA

import Download
import getQuestions

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = getQuestions.get_questions(data)
