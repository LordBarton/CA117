#!/usr/bin/env python3

import sys
import math

inp = [s.split() for s in sys.stdin.readlines()]

for s in inp:
    s = sorted([int(n) for n in s])
    sk = len(s) // 3
    if len(s) <= 3:
        print (sum(s[sk:]))
    else:
        print (sum(s[-3:]))
