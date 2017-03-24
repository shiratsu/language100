# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# めかぶと辞書配列の定義
# めかぶと辞書配列の定義
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')#文字列がGCされるのを防ぐ

aryInfo = []

i = 0
for line in open('neko.txt', 'r'):
    # if i == 10:
    #     break

    res = mecab.parseToNode(line)
    while res:
        dicWord = {}
        #単語を取得
        word = res.surface
        #品詞を取得
        # if len(res.feature) <= 2:
        #     print(res.feature)
        #     print(len(res.feature))
        aryRes = res.feature.split(",")
        # print(aryRes)
        if len(aryRes) > 7:
            dicWord['surface'] = word
            dicWord['base'] = aryRes[7]
            dicWord['pos'] = aryRes[1]
            dicWord['pos1'] = aryRes[2]
            aryInfo.append(dicWord)
        res = res.next

    # analyzetext = mecab.parse(line)
    # print(analyzetext)
    # aryNode = re.split("[\t,]",analyzetext)
    # print(aryNode)
    # print(aryNode[0])
    # if len(aryNode) > 2:
    #     dicWord = {}
    #     dicWord['surface'] = aryNode[0]
    #     dicWord['base'] = aryNode[7]
    #     dicWord['pos'] = aryNode[1]
    #     dicWord['pos1'] = aryNode[2]
    #     aryInfo.append(dicWord)
    # i += 1
print(aryInfo)
