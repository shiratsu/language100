#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 22.py

import re
from mymodule import extract_from_json

strCheck = r'\[\[Category:(.+)[\|\*|\|]?\]\]$'
strCheck2 = r'\[\[Category:(([^\|\*]+)|([^\|\*]+)[\||*]+)\]\]$'

lines = extract_from_json(u"イギリス").split("\n")
for line in lines:
    # print(line)
    # 連続した小文字のアルファベットを検索する
    matchObj = re.search(strCheck2, line)
    if matchObj:
        if matchObj.group(3):
            print(matchObj.group(3))
        else:
            print(matchObj.group(1))
        print(matchObj.groups())
