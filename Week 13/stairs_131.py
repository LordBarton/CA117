#!/usr/bin/env python3

import sys

inp = [s.strip() for s in sys.stdin.readlines()]

n = int(inp[0])

j = [int(j) for j in inp[1].split()]

ways = 0

for m in j:
    if n % m == 0:
        ways += 1
i = n
h = 0
while i > 0:
    if i - j[h] > 0:
        i -= j[h]
    else:
        if h + 1 < len(j):
            h += 1
        else:
            h = 0
    
