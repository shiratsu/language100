# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# 連続名詞を抽出して作成

# めかぶと辞書配列の定義
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')#文字列がGCされるのを防ぐ
aryInfo = []
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
            # print(aryNode[0])
            if aryNode[0] == '名詞' and prevWord == '' and intCount == 0:

                prevWord = word
                intCount += 1

            elif aryNode[0] == '名詞' and prevWord != '' and word != '' and intCount > 0:
                # print(word)
                print(prevWord)
                prevWord = prevWord+word
                intCount += 1

            elif aryNode[0] != '名詞' and prevWord != '' and intCount > 1:
                # print("------------------------------------")
                # print(prevWord)
                # print("------------------------------------")
                aryInfo.append(prevWord)
                prevWord = ''
                intCount = 0
            else:
                prevWord = ''
                intCount = 0

        res = res.next
print(aryInfo)
# print(str(aryInfo).decode("string-escape"))
