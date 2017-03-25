# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# 連続名詞を抽出して作成

# めかぶと辞書配列の定義
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')#文字列がGCされるのを防ぐ
dicInfo = {}
prevWord = ""
isMaking = False
intCount = 0

i = 0
for line in open('neko.txt', 'r'):

    # analyzetext = mecab.parse(line)
    # print(analyzetext)
    # print(line)
    res = mecab.parseToNode(line)
    # print(res)
    while res:
        #単語を取得
        word = res.surface
        #品詞を取得
        aryNode = res.feature.split(",")
        # print(aryRes)
        # print(word)
        if len(aryNode) > 7:
            if word in dicInfo:
                dicInfo[word] += 1
            else:
                dicInfo[word] = 0

        res = res.next
for k, v in sorted(dicInfo.items(), key=lambda x:x[1],reverse=True):
    print(k, v)
# print(str(aryInfo).decode("string-escape"))
