#!/usr/bin/env python3

import csv

previous = ""

with open("Lexique383.tsv", "r+", encoding="utf-8") as fd, open("dbpurifié.txt", "r+", encoding="utf-8", newline='') as file :

    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    pd = csv.writer(file, delimiter=' ')
    for x in range(18):
        next(rd)
    for row in rd:
        word = row[0]
        if len(word) > 7 :
            continue
        if word == previous :
            continue
        previous = word
        if " " in word :
            continue
        pd.writerow([row[0]])
