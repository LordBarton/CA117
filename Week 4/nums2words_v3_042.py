#!/usr/bin/env python3

import sys

file = sys.argv[1]
translation = {}

digits = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten"
}

f = open(file, 'r')
content = f.readlines()
for line in content:
    ls = line.strip().split()
    translation[ls[0]] = ls[1]

for line in sys.stdin:
    line = line.strip().split()
    out = [digits[int(n)] for n in line]
    translated = [translation[s] for s in out]
    print(" ".join(translated))
