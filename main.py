import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

import getQuestions
from RadarChart import getRadar
from TOPSIS import topsis

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = getQuestions.get_questions(data)

keys = list(questions.keys())
X = pd.DataFrame(questions).T

pca = PCA()
line = pca.fit(X)
plt.plot([1, 2, 3, 4], np.cumsum(pca.explained_variance_ratio_))
plt.xticks([1, 2, 3, 4])
plt.xlabel("Number of Components after Dimension Reduction")
plt.ylabel("Cumulative Explained Variance Ratio")
plt.show()

pca = PCA(n_components=0.95)
X_reduction = pca.fit_transform(X)
print(pca.explained_variance_ratio_)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)
ax.scatter([x[0] for x in X_reduction], [x[1] for x in X_reduction])
ax.grid()
plt.show()

temp = list()
for x in X_reduction:
    temp.append(x[0] * pca.explained_variance_ratio_[0] + x[1] * pca.explained_variance_ratio_[1])
# temp = [max(temp) - x for x in temp]
# sqSum = 0
# for item in temp:
#     sqSum += item ** 2
# temp = np.array([x / np.sqrt(sqSum) for x in temp])
temp = [(x - min(temp)) / (max(temp) - min(temp)) * 100 for x in temp]
ans = np.column_stack((keys, temp))
var = pd.DataFrame(sorted(ans, key=lambda x: int(x[0])))

index = 0
for key in keys:
    questions[key] = temp[index]
    index += 1

problemTypes = ["字符串", "线性表", "数组", "查找算法", "数字操作", "图结构", "树结构", "排序算法"]

fp = open("code_analysis/code_result.json", "r", encoding="UTF-8")
codeRes = json.load(fp)
users = data.keys()
problemString = dict()
problemLinkedList = dict()
problemArray = dict()
problemSearch = dict()
problemNumeric = dict()
problemGraph = dict()
problemTree = dict()
problemSort = dict()
for user in users:
    for problemType in problemTypes:
        if problemType is problemTypes[0]:
            problemString[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[1]:
            problemLinkedList[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[2]:
            problemArray[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[3]:
            problemSearch[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[4]:
            problemNumeric[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[5]:
            problemGraph[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[6]:
            problemTree[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])
        elif problemType is problemTypes[7]:
            problemSort[user] = (
                sum([problem.get("final_score") * questions.get((problem.get("case_id"), problemType), 0)
                     for problem in data.get(user).get("cases")]), codeRes.get(user)[3])

ansString = pd.DataFrame(problemString).T
ansString = topsis(ansString, [0.8, 0.2])
ansLinkedList = pd.DataFrame(problemLinkedList).T
ansLinkedList = topsis(ansLinkedList, [0.8, 0.2])
ansArray = pd.DataFrame(problemArray).T
ansArray = topsis(ansArray, [0.8, 0.2])
ansSearch = pd.DataFrame(problemSearch).T
ansSearch = topsis(ansSearch, [0.8, 0.2])
ansNumeric = pd.DataFrame(problemNumeric).T
ansNumeric = topsis(ansNumeric, [0.8, 0.2])
ansGraph = pd.DataFrame(problemGraph).T
ansGraph = topsis(ansGraph, [0.8, 0.2])
ansTree = pd.DataFrame(problemTree).T
ansTree = topsis(ansTree, [0.8, 0.2])
ansSort = pd.DataFrame(problemSort).T
ansSort = topsis(ansSort, [0.8, 0.2])
getRadar([ansString.loc["60606", "综合得分指数"] * 100,
          ansLinkedList.loc["60606", "综合得分指数"] * 100,
          ansArray.loc["60606", "综合得分指数"] * 100,
          ansSearch.loc["60606", "综合得分指数"] * 100,
          ansNumeric.loc["60606", "综合得分指数"] * 100,
          ansGraph.loc["60606", "综合得分指数"] * 100,
          ansTree.loc["60606", "综合得分指数"] * 100,
          ansSort.loc["60606", "综合得分指数"] * 100])
