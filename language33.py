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

    res = mecab.parseToNode(line)
    # print(aryNode)
    # print(res)
    while res:
        #単語を取得
        word = res.surface
        #品詞を取得
        pos = res.feature.split(",")[0]
        pos2 = res.feature.split(",")[1]
        if pos == '名詞' and pos2 == 'サ変接続':
            print(word)
        res = res.next

    # if len(aryNode) > 2:
    #     if aryNode[1] == '名詞' and aryNode[2] == 'サ変接続':
    #         print(aryNode[0])
