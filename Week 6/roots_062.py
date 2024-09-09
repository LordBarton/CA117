#!/usr/bin/env python3

import sys
import math

input = [s.strip() for s in sys.stdin.readlines()]

def roots(input):
    out = []
    for line in input:
        line = line.split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])

        D = b ** 2 - 4 * (a * c)

        if D < 0:
            out.append(None)
        else:
            x1 = (-b - math.sqrt(D)) / (2 * a)
            x2 = (-b + math.sqrt(D)) / (2 * a)
            r = sorted([x1, x2])
            r = [str(round(x, 1)) for x in r]
            out.append(", ".join(r))
    for s in out:
        print(s)
roots(input)
