#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

n = int(lines[0].strip())
c = lines[1].split()
total = 0
i = 0
while i < len(c) and total + int(c[i]) <= n:
    total += int(c[i])
    i += 1
print(i)
