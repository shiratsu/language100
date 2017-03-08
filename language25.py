import re
from mymodule import extract_from_json

strCheck = r'\{\{基礎情報.+\}\}$'
strKiso = r'[^\|]+\s?=\s?.+'
lines = extract_from_json(u"イギリス").split("\n")
kisoFlag = False
dict = {}

for line in lines:

    if line == '{{基礎情報 国':
        print("true")
        kisoFlag = True
        continue
    elif kisoFlag == True and line != '}}':
        # 連続した小文字のアルファベットを検索する
        # print(line)
        matchObj = re.search(strKiso, line)
        if matchObj:
            tmp = matchObj.group()
            # print(tmp)
            aryKiso = tmp.split("=")
            # print(aryKiso)
            dict.update({aryKiso[0].strip(): aryKiso[1].strip()})
    elif line == '}}':
        print("false")
        kisoFlag = False
        continue

print(dict)
