# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# めかぶと辞書配列の定義
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')#文字列がGCされるのを防ぐ
aryInfo = []
prevWord = ""
isMaking = False

i = 0
for line in open('neko.txt', 'r'):
    if i == 10:
        break
    i += 1
    # analyzetext = mecab.parse(line)
    # print(analyzetext)
    # print(line)
    res = mecab.parseToNode(line)
    # print(res)
    while res:
        #単語を取得
        word = res.surface
        #品詞を取得
        pos = res.feature.split(",")[1]
        print('{0} , {1}'.format(word, pos))
        #次の単語に進める
        res = res.next


    # aryNode = re.split("[\t,]",analyzetext)
    # print(aryNode)
    # if len(aryNode) > 2:
    #     if aryNode[1] == '名詞' and prevWord == '' and isMaking == False:
    #         print(aryNode[0])
    #         prevWord = aryNode[0]
    #         isMaking = True
    #     elif aryNode[1] == '助詞' and aryNode[0] == 'の' and prevWord != '' and isMaking == True:
    #         print(aryNode[0])
    #         print(prevWord)
    #         prevWord = prevWord+aryNode[0]
    #     elif aryNode[1] == '名詞' and prevWord != '' and aryNode[0] != '' and isMaking == True:
    #         print(aryNode[0])
    #         print(prevWord)
    #         prevWord = prevWord+aryNode[0]
    #         print(prevWord)
    #         aryInfo.append(prevWord)
    #         prevWord = ''
    #         isMaking = False
    #     elif prevWord != '' and isMaking == True and aryNode[1] != '名詞' and aryNode[1] != '助詞':
    #         prevWord = ''
    #         isMaking = False

print(aryInfo)
