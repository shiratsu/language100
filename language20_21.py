#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 20.py

import json
from mymodule import extract_from_json

with open("../language100_another/jawiki-country.json") as f:

    # １行ずつ読み込む
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == u"イギリス":
            print(article_dict["text"])
        article_json = f.readline()

print("======================================================================")

lines = extract_from_json(u"イギリス")
for line in lines:
    if line == "Category":
        print(line)
