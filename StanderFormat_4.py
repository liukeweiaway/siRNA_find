#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2019/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------
# import pandas as pd
# pdd = pd.read_csv('results.txt', sep=' ', header=None)
# startBase = pdd[4]
# endBase = pdd[6]
# sequence = pdd[3]
# TrueEnerge = pdd[2]
# print(pdd.values[:, [2,3,4,6]])
# d = {k: v for k, v in dic.items() if v >=2}
import operator

sesDict = {}

with open('results.txt', 'r') as inputFile:
    for line in inputFile.readlines():
        cells = line.strip().split()
        key = ''.join(cells[2:9])
        # print(type(key), type(cells[3]))
        print(key)
        if key in sesDict.keys():
            sesDict[key] += 1
        else:
            sesDict[key] = 1

sorted_x = sorted(sesDict.items(), key=operator.itemgetter(1), reverse=True)
with open('resultsSorted.txt', 'w') as outpuFile:
    for i in sorted_x:
        print(*i, sep=',', file=outpuFile)
