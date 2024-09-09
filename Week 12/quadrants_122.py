#!/usr/bin/env python3

import sys

inp = [s for s in sys.stdin.readlines()]

for s in inp:
    ns = [int(n) for n in s.split()]
    if ns[0] * ns[1] > 0:
        if ns[0] > 0:
            print(1)
        else:
            print(3)
    else:
        if ns[0] < 0:
            print(4)
        else:
            print(2)
