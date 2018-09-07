#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re, sys

filepath = sys.argv[1]
outpath = sys.argv[2]
contents = []
with open(filepath, "r") as fin:
    contents = fin.read()
with open(outpath, "w") as fout:
    for i in range(len(contents)):
        fout.write('{:>3}'.format(ord(contents[i])))
        fout.write(",")
        if (i+1)%15 == 0:
            fout.write("\n")
        