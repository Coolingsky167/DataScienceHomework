import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

import getQuestions

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
temp = [max(temp) - x for x in temp]
# sqSum = 0
# for item in temp:
#     sqSum += item ** 2
# temp = np.array([x / np.sqrt(sqSum) for x in temp])
temp = [(x - min(temp)) / (max(temp) - min(temp)) * 100 for x in temp]
for item in temp:
    if item < 25:
        print(questions.get(keys[temp.index(item)]))
ans = np.column_stack((X_reduction, temp))
