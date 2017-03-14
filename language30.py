# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# めかぶと辞書配列の定義
mecab = MeCab.Tagger('mecabrc')

aryInfo = []

i = 0
for line in open('neko.txt', 'r'):
    if i == 10:
        break

    analyzetext = mecab.parse(line)
    print(analyzetext)
    aryNode = re.split("[\t,]",analyzetext)
    print(aryNode)
    print(aryNode[0])
    if len(aryNode) > 2:
        dicWord = {}
        dicWord['surface'] = aryNode[0]
        dicWord['base'] = aryNode[7]
        dicWord['pos'] = aryNode[1]
        dicWord['pos1'] = aryNode[2]
        aryInfo.append(dicWord)
    i += 1
print(aryInfo)
