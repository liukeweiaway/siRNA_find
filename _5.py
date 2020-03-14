#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2019/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------
import re

outputFile = open('fResults.txt', 'w')

with open('resultsSorted.txt', 'r') as inputFile:
    for line in inputFile.readlines():
        cells = re.split('\^|:|,|!', line.strip())
        # print('cells', cells)
        with open('results.txt', 'r') as inputFile2:
            for line2 in inputFile2.readlines():
                if cells[1] in line2:
                    if cells[2] in line2:
                        if cells[3] in line2:
                            cells2 = line2.split()
                            # print(cells, cells2)
                            # print('cells2', cells2)
                            print(cells2[10], cells[0], cells[1], cells[2], cells[4], cells2[0], cells2[1], sep=',', file=outputFile)
                            break
outputFile.close()
