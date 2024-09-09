#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

seen = []
for s in lines:
    s = s.strip().split()
    for w in s:
        w = w.strip(",").strip(".").strip(":").lower()
        if "--" not in w and w not in seen:
            seen.append(w)
seen.sort()
print(len(seen))
