import json
import urllib.request
import urllib.parse
import os
import zipfile


def download(data, root):
    """
    将下载下来的文件放在root目录下,同时修改各个代码的url为本地资源（下载下来保存的位置）,并将修改后的数据写入对应的_downloaded.json文件
    :param data:由sample.json或者test_data.json转换而来的字典，包含要下载的文件的url
    :param root:下载下来的资源要保存的根目录
    :return:None
    """
    if not os.path.isdir(root):
        os.mkdir(root)
    for key in data.keys():
        user_path = root+'\\'+key
        if not os.path.isdir(user_path):
            os.mkdir(user_path)
        cases = data[key]["cases"]
        for i in range(len(cases)):
            case = cases[i]
            case_path = user_path+'\\'+case['case_id'] + '\\'
            if not os.path.isdir(case_path):
                os.mkdir(case_path)
            case_zip = case["case_zip"]
            filename = urllib.parse.unquote(os.path.basename(case_zip))
            filename = filename.replace('*', '_')
            if not os.path.isdir(case_path+filename[0:-4]):
                case_zip = 'http:' + urllib.parse.quote(case_zip[5:])
                # print(case_zip)
                urllib.request.urlretrieve(case_zip, case_path + filename)
                case_file = zipfile.ZipFile(case_path+filename)
                filename = filename[0:-4]
                os.mkdir(case_path+filename)
                for names in case_file.namelist():
                    case_file.extract(names, case_path+filename)
                case_file.close()
                os.remove(case_path + filename + '.zip')
                data[key]['cases'][i]['case_zip'] = case_path + filename + '\\'
            else:
                data[key]['cases'][i]['case_zip'] = case_path + filename[0:-4] + '\\'
            case_path += 'upload_records'+'\\'
            if not os.path.isdir(case_path):
                os.mkdir(case_path)
            upload_records = case['upload_records']
            # print(data[key]['cases'][i]['case_zip'])
            for j in range(len(upload_records)):
                upload_record = upload_records[j]
                upload_path = case_path+str(upload_record['upload_id'])+'\\'
                code_url = upload_record['code_url']
                data[key]['cases'][i]['upload_records'][j]['code_url'] = upload_path
                # print('    ' + data[key]['cases'][i]['upload_records'][j]['code_url'])
                filename = urllib.parse.unquote(os.path.basename(code_url))
                # print(upload_path)
                # print(filename)
                # print(code_url)
                if not os.path.isdir(upload_path):
                    os.mkdir(upload_path)
                else:
                    continue
                urllib.request.urlretrieve(code_url, upload_path+filename)
                upload_file = zipfile.ZipFile(upload_path+filename)
                for names in upload_file.namelist():
                    upload_file.extract(names, upload_path)
                    if names.endswith('.zip'):
                        zip_file = zipfile.ZipFile(upload_path+names)
                        for name in zip_file.namelist():
                            zip_file.extract(name, upload_path)
                        zip_file.close()
                        os.remove(upload_path+names)
                upload_file.close()
                os.remove(upload_path + filename)


# sample代码放在code_sample目录下,test_data代码放在code目录下
if __name__ == '__main__':
    # fp = open("../sample.json", "r", encoding="UTF-8")
    # Data = json.load(fp)
    # download(Data, 'code_sample')
    # Data = json.dumps(Data, indent=4)
    # with open('../sample_downloaded.json', 'w', encoding='UTF-8') as f:
    #     f.write(Data)
    fp = open("../test_data.json", "r", encoding="UTF-8")
    Data = json.load(fp)
    download(Data, 'code')
    Data = json.dumps(Data, indent=4)
    with open("../test_data_downloaded.json", 'w') as f:
        f.write(Data)


