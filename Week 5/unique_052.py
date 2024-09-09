#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

for line in input:
    line = line.split()
    nums = [int(n) for n in line if line.count(n) == 1]
    if len(nums) == 0:
        print("none")
    else:
        print(max(nums))
