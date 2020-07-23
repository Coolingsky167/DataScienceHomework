import json
import urllib.request
import urllib.parse
import os


def download(data):
    if isinstance(data, dict):
        for key in data.keys():
            cases = data[key]["cases"]
            for case in cases:
                case_zip = case["case_zip"]
                filename = urllib.parse.unquote(os.path.basename(case_zip))
                case_zip = 'http:'+urllib.parse.quote(case_zip[5:])
                print(case_zip)
                urllib.request.urlretrieve(case_zip, filename)


if __name__ == '__main__':
    fp = open("sample.json", "r", encoding="UTF-8")
    data = json.load(fp)
    download(data)

