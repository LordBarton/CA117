#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

def swap(input):
    cups = ['1','2','3']
    pos = int(input[0])
    cups[pos - 1] = "p"
    seq = [a for a in input[1]]
    for t in seq:
        if t == "A":
            temp = cups[0]
            cups[0] = cups[1]
            cups[1] = temp
        elif t == "B":
            temp = cups[1]
            cups[1] = cups[2]
            cups[2] = temp
        elif t == "C":
            temp = cups[0]
            cups[0] = cups[2]
            cups[2] = temp
    return cups.index("p") + 1
print(swap(input))
