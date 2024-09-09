#!/usr/bin/env python3

import sys

inp = [s.lower().strip() for s in sys.stdin.readlines()]

def simplicity(s):

    seen = {}
    for lt in s:
        if lt not in seen:
            seen[lt] = 1
        else:
            seen[lt] += 1
    return seen

for s in inp:
    freq = simplicity(s)
    lvl = len(freq)
    if lvl <= 2:
        print(0)
    else:
        final = 0
        while lvl > 2:
            least = min(freq.values())
            least_k = [k for k, v in freq.items() if v == least][0]
            final += least
            lvl -= 1
            del freq[least_k]
        print(final)
