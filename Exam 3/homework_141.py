#!/usr/bin/env python3

import sys

s = sys.stdin.read().strip()

s = s.split(';')

total = 0
for n in s:
    if '-' in n:
        temp = n.split('-')
        st = int(temp[0])
        en = int(temp[1])
        if st == 0:
            total += en
        else:
            i = st - 1
            t = 0
            while i < en:
                t += 1
                i += 1
            total += t
    else:
        total += 1

print (total)
