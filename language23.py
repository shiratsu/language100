#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 23.py

import re
from mymodule import extract_from_json

strCheck = r'(^=[\s]?([^=]+)=[\s]?$)|(^==[\s]?([^=]+)==[\s]?$)|(^===[\s]?([^=]+)===[\s]?$)'

lines = extract_from_json(u"イギリス").split("\n")
for line in lines:
    # print(line)
    # 連続した小文字のアルファベットを検索する
    matchObj = re.search(strCheck, line)
    if matchObj:
        print(matchObj.groups())
        # if len(matchObj.group(1)) == 2:
        #     print(matchObj.group(0),1)
        # else:
        #     print(matchObj.group(0),2)
