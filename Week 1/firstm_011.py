#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for s in lines:
    s = s.strip()
    i = 0
    while s[i] != "m" and i < len(s) - 1:
        i += 1
    if i == len(s) - 1:
        print(s)
    else:
        print(s[:i] + s[i].capitalize() + s[i + 1:])
