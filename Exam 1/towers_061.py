#!/usr/bin/env python3

import sys

line = [int(s) for s in sys.stdin.readline().split()]

def towers(line):
    i = 1
    towers = 1
    base = line[0]
    while i < len(line):
        if line[i] > base:
            towers = towers + 1
        base = line[i]
        i += 1
    return towers

print(towers(line))
