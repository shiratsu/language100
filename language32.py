# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# めかぶと辞書配列の定義
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')#文字列がGCされるのを防ぐ

aryInfo = []

i = 0
for line in open('neko.txt', 'r'):

    res = mecab.parseToNode(line)
    while res:
        #単語を取得
        word = res.surface
        #品詞を取得
        aryRes = res.feature.split(",")
        # print(aryRes)
        if len(aryRes) > 7:
            #品詞を取得
            pos = aryRes[1]
            viewWord = aryRes[7]
            if pos == '動詞':
                print(viewWord)
        res = res.next
    # if len(aryNode) > 2:
    #     if aryNode[1] == '動詞':
    #         print(aryNode[7])
