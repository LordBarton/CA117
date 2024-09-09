#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()
words = []
for lines in input:
    words.extend([s.lower().strip('.').strip('?').strip('...') for s in lines.split()])

dict = {}

for word in sorted(words):
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

for k, v in dict.items():
    print(f'{k} : {v}')
