#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()

def times(input):
    mdict = {}
    keys_to_remove = []
    for line in input:
        line = line.split()
        name = line[0]
        if name not in mdict:
            mdict[name] = []
        for w in line:
            if ':' in w and w not in mdict[name]:
                mdict[name].append(w)
    for k,v in mdict.items():
        best_time = float('inf')
        sbest_time = None

        for item in v:
            try:
                v2 = item.split(':')
                v2 = int(v2[0]) * 60 + int(v2[1])
                if v2 < best_time:
                    best_time = v2
                    sbest_time = item
            except ValueError:
                keys_to_remove.append(k)

        mdict[k] = sbest_time, best_time

    for r in keys_to_remove:
        del mdict[r]

    return mdict

runners = times(input)

best_time = float('inf')
for k, v in runners.items():
    if v[1] < best_time:
        best_time = v[1]
        winner = k
        time = v[0]
print(f'{winner} : {time}')
