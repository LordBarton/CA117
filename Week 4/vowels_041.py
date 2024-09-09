#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

dict = {}
vowels = ['a', 'e', 'i', 'o', 'u']
for line in lines:
    for s in line.lower():
        if s not in dict and s in vowels:
            dict[s] = 1
        elif s in dict:
            dict[s] += 1

max_v_width = len(str(max(dict.values())))
def tagger(item):
   return item[1]
for k,v in sorted(dict.items(), key=tagger, reverse=True):
    print(f'{k} : {v:>{max_v_width}d}')
