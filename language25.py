#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 23.py

import re
from mymodule import extract_from_json

strCheck = r'\{\{基礎情報.+\}\}$'

lines = re.split(r"\n[\|}]", extract_from_json(u"イギリス"))
for line in lines:
    # print(line)
    # 連続した小文字のアルファベットを検索する
    print(line)
    
