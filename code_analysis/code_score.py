import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import json


def get_code_scores():
    fp = open('code_features.json', 'r', encoding='UTF-8')
    code_features = json.load(fp)
    X = pd.DataFrame(code_features).T
    X_pred = KMeans(n_clusters=3, n_jobs=-1).fit_predict(X)
    score = metrics.calinski_harabasz_score(X, X_pred)
    print(X)
    print(X_pred)
    keys = code_features.keys()
    for i in range(len(keys)):
        code_features[keys[i]].append(X_pred[i])
    print(code_features)


if __name__ == '__main__':
    get_code_scores()