#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for s in lines:
    s = s.strip()
    if len(s) % 2 != 0:
        print(s[len(s) // 2])
    else:
        print("No middle character!")
