import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn import preprocessing
import json


def get_score():
    fp = open('code_features.json', 'r', encoding='UTF-8')
    code_features = json.load(fp)
    X = pd.DataFrame(code_features).T
    # X_scaled = preprocessing.scale(X)
    X_pred = KMeans(n_clusters=3).fit_predict(X)
    # print(X_pred)
    score = metrics.calinski_harabasz_score(X, X_pred)
    keys = list(code_features.keys())
    for i in range(len(keys)):
        code_features[keys[i]] = X_pred[i]
    code_features = sorted(code_features.items(), key=lambda x: x[1])
    return code_features
    # for i in range(len(code_features)):
    #     print(code_features[i])

print(get_score())