#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for s in lines:
    s = s.strip()
    spl = s.split('@')
    name = spl[0].split('.')
    first = name[0]
    last = ""
    for ch in name[1]:
        if ch < "0" or ch > "9":
            last += ch
    print(first.capitalize(), last.capitalize())
