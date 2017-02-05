#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 06.p
input1 = "paraparaparadise"
input2 = "paragraph"

X = []
Y = []


def ngram2(input, n):

    list = []
    # 文字 n-gram (引数 str)
    l = len(input)
    if type(input) == str:
        for i in xrange(l):
            list.append(input[i:i+n])
    return list

X = ngram2(input1,2)
Y = ngram2(input2,2)

print(set(X).union(set(Y)))
print(set(X).difference(set(Y)))
print(set(X).intersection(set(Y)))
