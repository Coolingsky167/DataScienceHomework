import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from download import Download
import getQuestions

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = getQuestions.get_questions(data)

keys = questions.keys()
X = pd.DataFrame([x for x in
                  [questions.get(key) for key in keys]])

pca = PCA(n_components=0.95)
X_reduction = pca.fit_transform(X)
print(pca.explained_variance_ratio_)
for x in X_reduction:
    print(x[0] * pca.explained_variance_ratio_[0] + x[1] * pca.explained_variance_ratio_[1])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)
ax.scatter([x[0] for x in X_reduction], [x[1] for x in X_reduction])
ax.grid()
plt.show()
