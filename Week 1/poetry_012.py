#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

max_length = 0
for s in lines:
    s = s.strip()
    if len(s) > max_length:
        max_length = len(s)

for s in lines:
    s = s.strip()
    mid = (max_length - len(s)) // 2
    spaces = max_length - (mid + len(s))
    print((f'{s:>{mid + len(s)}}') + " " * spaces)
