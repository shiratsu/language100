#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

input = input.replace(":","")
input = input.replace(".","")

list = []

someHandleWord(input)

def someHandleWord(strWord):
    print(strWord)

    arystr = strWord.split(" ")

    for word in arystr:
        #長さを取得
        l = len(word)
        if l < 5:
            list.append(word)
        else:
            aryChar = list(word)
            aryTmp = aryChar
            random.shuffle(aryTmp)
            addStr = aryChar[0]+aryTmp[1:len(aryTmp)-2]+aryChar[1]
            list.append(addStr)

    print(list)
