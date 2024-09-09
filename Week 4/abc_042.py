#!/usr/bin/env python3

import sys

nums = [int(n) for n in sys.stdin.readline().strip().split()]

letters = list(sys.stdin.readline().strip())

abc = "ABCDEF"
ordered = {}

i = 0
while i < 6:
    ordered[abc[i]] = sorted(nums)[i]
    i += 1

out = [str(ordered[s]) for s in letters]
print(" ".join(out))
