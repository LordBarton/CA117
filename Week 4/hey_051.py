#!/usr7Bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

def hey(input):
    for s in input:
        e = s.count('e') * 2
        print('h' + 'e' * e + 'y')

hey(input)
