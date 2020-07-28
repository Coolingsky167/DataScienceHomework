import json
import os
from typing import Dict, AnyStr
import pylint


# 得到每个学生做的每道题的代码路径
def get_code_path(data):
    code = {}
    for key in data.keys():
        code[key] = {}
        cases = data[key]['cases']
        for case in cases:
            code[key][case['case_id']] = case['case_zip']+'.mooctest\\'
    return code


# 利用pylint分析代码规范程度,并输出到代码下面的pylint_result.txt文件中
def pylint_code(code):
    for key1 in code.keys():
        for key2 in code[key1].keys():
            base_path = code[key1][key2]
            base_path = '..\\'+base_path
            if not os.path.exists(base_path+'pylint_result.txt'):
                print(key1+'  '+key2)
                f = open(base_path + 'pylint_result.txt', 'w')
                pylint.epylint.py_run(base_path + 'answer.py', return_std=True, stdout=f, stderr=f)
                f.close()
            # if os.path.exists(base_path + 'pylint_result.txt'):
            #     print('      ' + key2)
            #     os.remove(base_path + 'pylint_result.txt')


def extract_code_features(code: Dict):
    code_score = {}
    for key1 in code.keys():
        pylint_scores = []
        magic_counts = []
        count = 0
        for key2 in code[key1].keys():
            base_path = code[key1][key2]
            base_path = '..\\' + base_path
            if not os.path.exists(base_path+'pylint_result.txt'):
                continue
            print(key1+'    '+key2)
            count += 1
            score = get_pylint_score(base_path+'pylint_result.txt')
            if score != 20:
                pylint_scores.append(score)
                magic_counts.append(get_code_count(base_path+'answer.py'))
        n = len(pylint_scores)
        code_score[key1] = [
            sum(pylint_scores) / n,
            sum(magic_counts) / n,
            # len(code[key1].keys()) - n
            (count - n) / count
        ]
    return code_score


# 获取经pylint分析得到的代码规范得分(最高得分为10分),20表示pylint分析出异常了,此时代码非python3代码
def get_pylint_score(path: AnyStr):
    if not os.path.exists(path):
        return 20
    pylint_result = open(path, 'r', encoding='utf-8')
    lines = pylint_result.readlines()
    n = len(lines)
    if n <= 3:
        return 20
    else:
        line = lines[-5].lstrip('Your code has been rated at ')
        index = line.find('/')
        if index != -1:
            return float(line[0:index])
        else:
            return 20


# 统计代码中if,elif,else,字面常量的数量
def get_code_count(path: AnyStr):
    cur_code = open(path, 'r', encoding='utf-8')
    count = 0
    for line in cur_code.readlines():
        count += line.count('if')*2+line.count('elif')*4+line.count('else')*4
        for c in line:
            if c.isdigit():
                count += 1
    return count


if __name__ == '__main__':
    # fp = open('sample_downloaded.json', 'r', encoding='UTF-8')
    fp = open('../test_data_downloaded.json', 'r', encoding='UTF-8')
    data = json.load(fp)
    code = get_code_path(data)
    # pylint_code(code)
    code_features = extract_code_features(code)
    code_features = json.dumps(code_features, indent=4)
    with open('code_features.json', 'w', encoding='UTF-8') as f:
        f.write(code_features)
        # f.write('\n\n\n\n\n')


