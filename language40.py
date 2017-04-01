# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib.font_manager import FontProperties
import CaboCha

class Morph:
    surface = ''
    base = ''
    pos = ''
    pos1 = ''

    def __init__(self,line):
        cp = CaboCha.Parser('-f1')
        tree = cp.parse(line)
        print(line)
        print(tree.toString(CaboCha.FORMAT_TREE))
        chunk_dic = {}
        chunk_id = 0
        for i in range(0, tree.size()):
            token = tree.token(i)
            if token.chunk:
                chunk_dic[chunk_id] = token.chunk
                chunk_id += 1

        tuples = []
        for chunk_id, chunk in chunk_dic.items():
            if chunk.link > 0:
                self.get_word(tree, chunk)


    def get_word(self,tree, chunk):
        surface = ''
        for i in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
            token = tree.token(i)
            features = token.feature.split(',')
            pos = features[0]
            pos1 = features[1]
            surface = features[7]
            base = token.surface
            print(features)
            print(base)

if __name__ == '__main__' :
    i = 0
    for line in open('neko.txt', 'r'):
        if i > 3:
            break
        m = Morph(line)
        i += 1
