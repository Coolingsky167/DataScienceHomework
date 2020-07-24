import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import Download
import getQuestions

fp = open("test_data.json", "r", encoding="UTF-8")
data = json.load(fp)

questions = getQuestions.get_questions(data)

keys = questions.keys()
X = pd.DataFrame([x for x in [questions.get(key) for key in keys]])

pca = PCA(n_components=0.95)
X_reduction = pca.fit_transform(X)
for x in X_reduction:
    print(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)
ax.scatter([x[0] for x in X_reduction], [x[1] for x in X_reduction], alpha=0.8)
ax.grid()
plt.show()
