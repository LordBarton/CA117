#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

for lines in s:
    lines = lines[1:-2].strip()
    if len(lines) > 0:
        print(lines)
