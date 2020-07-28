import os
import json



def name_filter(data):
    """
    对解压缩出来的文件名进行处理,去掉其中的' ',方便后续pylint处理(pylint不能处理路径中带有空格的py文件)
    :param data:
    :return:
    """
    for key in data.keys():
        cases = data[key]["cases"]
        for i in range(len(cases)):
            case_zip = cases[i]['case_zip']
            data[key]['cases'][i]['case_zip'] = case_zip.replace(' ', '')
            s = data[key]['cases'][i]['case_zip']
            if case_zip != s and not os.path.exists(s):
                os.rename(case_zip, data[key]['cases'][i]['case_zip'])


if __name__ == '__main__':
    fp = open('../test_data_downloaded.json', 'r', encoding='UTF-8')
    Data = json.load(fp)
    name_filter(Data)
    Data = json.dumps(Data, indent=4)
    with open("../test_data_downloaded.json", 'w') as f:
        f.write(Data)