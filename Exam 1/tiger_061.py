#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

def count(input):
    for line in input:
        bars = line.count('|')
        if bars % 2 == 0:
            print('safe')
        else:
            print('unsafe')
count(input)
