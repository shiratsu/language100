#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 25.py

import re
from mymodule import extract_from_json

strCheck = r'\{\{基礎情報.+\}\}$'
strKiso = r'[^\|]+\s?=\s?.+'
strMoji = r'\'+(.)+\'+'
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
            key = aryKiso[0].strip()
            val = aryKiso[1].strip()
            print(key)
            matchObjKey = re.search(strMoji, key)
            matchObjVal = re.search(strMoji, key)

            if matchObjVal and matchObjKey:
                # print(matchObjVal.group(0))
                # print(matchObjVal.group(1))
                # print(matchObjKey.group(0))
                # print(matchObjKey.group(1))

                dict.update({matchObjKey.group(1): matchObjVal.group(1)})

            # print(aryKiso)
            # dict.update({aryKiso[0].strip(): aryKiso[1].strip()})
    elif line == '}}':
        print("false")
        kisoFlag = False
        continue

print(dict)
