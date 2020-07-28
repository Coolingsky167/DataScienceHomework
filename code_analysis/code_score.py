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
    # X_pred = KMeans(n_clusters=3).fit_predict(X_scaled)
    X_pred = KMeans(n_clusters=3).fit_predict(X)
    # print(X_pred)
    score = metrics.calinski_harabasz_score(X, X_pred)
    print(score)
    keys = list(code_features.keys())
    for i in range(len(keys)):
        code_features[keys[i]].append(float(X_pred[i]))
    code_features = sorted(code_features.items(), key=lambda x: x[1][3])
    temp = {}
    for i in range(len(code_features)):
        print(code_features[i])
        temp[code_features[i][0]] = code_features[i][1]
    temp = json.dumps(temp, indent=4)
    with open('code_scores.json', 'a', encoding='UTF-8') as f:
        f.write(temp)
        f.write('\n\n\n\n')


def authorize():
    fp = open('code_scores.json', 'r', encoding='UTF-8')
    data = json.load(fp)
    for key in data.keys():
        num = data[key][3]
        if num == 0.0:
            data[key][3] = 2.0
        elif num == 2.0:
            data[key][3] = 3.0
    data = json.dumps(data, indent=4)
    with open('code_scores.json', 'w', encoding='UTF-8') as f:
        f.write(data)


if __name__ == '__main__':
    # get_score()
    # authorize()
    pass