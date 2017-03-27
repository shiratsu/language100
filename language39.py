# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'/Library/Fonts/TTEditHalfGothic.ttf', size=14)

# めかぶと辞書配列の定義
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')#文字列がGCされるのを防ぐ

dicInfo = {}
for line in open('neko.txt', 'r'):

    res = mecab.parseToNode(line)
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

i = 0
left = np.array( [] )
height = np.array( [] )
axis = []
for k, v in sorted(dicInfo.items(), key=lambda x:x[1],reverse=True):

    if i >= 10:
        break;

    axis.append(k)
    left = np.append( left, i )
    height = np.append( height, v )
    i += 1

# 上位何個かを棒グラフで表示
plt.xticks(left, axis, fontproperties=fp)
plt.plot(left, height,'r')
plt.show()

# left = np.array([1, 2, 3, 4, 5])
# height = np.array([100, 200, 300, 400, 500])
# plt.bar(left, height)
