#!/usr/bin/env python3

import sys

input = [s.lower().strip() for s in sys.stdin.readlines()]
vowels = "aeiou"
final = {}

for s in input:
    total = 0
    for v in vowels:
        total += s.count(v) // 2
    final[s] = total

keymax = max(zip(final.values(), final.keys()))[1]

print (keymax)
