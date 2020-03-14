#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2019/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------
import pandas as pd
import os


def findsiRNAL(inputFile, folder, outputFile, siRNAL):
    filePath = folder + '/' + file
    pdd = pd.read_csv(filePath, sep=' ', header=None)
    energes = pdd.values[:, 4]
    sequence = pdd.values[:, 1]
    with open(outputFile, 'a') as outputFile:
        for num, eneger in enumerate(energes):
            if list(energes[num:num+siRNAL]).count(0) == siRNAL-3:
                print(siRNAL, '3', ''.join(sequence[num:num + siRNAL]), '^', num + 1 + (int(folder)-1) * 1500, ':', num + siRNAL + (int(folder)-1) * 1500, '!', 'folder' + str(folder), '!', inputFile, file=outputFile)
            elif list(energes[num:num+siRNAL]).count(0) == siRNAL-2:
                print(siRNAL, '2', ''.join(sequence[num:num + siRNAL]), '^', num + 1 + (int(folder)-1) * 1500, ':', num + siRNAL + (int(folder)-1) * 1500, '!', 'folder' + str(folder), '!', inputFile, file=outputFile)
            elif list(energes[num:num+siRNAL]).count(0) == siRNAL-1:
                print(siRNAL, '1', ''.join(sequence[num:num + siRNAL]), '^', num + 1 + (int(folder)-1) * 1500, ':', num + siRNAL + (int(folder)-1) * 1500, '!', 'folder' + str(folder), '!', inputFile, file=outputFile)
            elif list(energes[num:num+siRNAL]).count(0) == siRNAL-0:
                print(siRNAL, '0', ''.join(sequence[num:num + siRNAL]), '^', num + 1 + (int(folder)-1) * 1500, ':', num + siRNAL + (int(folder)-1) * 1500, '!', 'folder' + str(folder), '!', inputFile, file=outputFile)


folders = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
for folder in folders:
    print(folder)
    siRNALs = [21, 22, 23, 24, 25]
    files = os.listdir(folder)
    outputFile = 'results.txt'
    for file in files:
        for siRNAL in siRNALs:
            findsiRNAL(file, folder, outputFile, siRNAL)
