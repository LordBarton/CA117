#!/usr/bin/env python3

import sys

digits = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten"
}

for line in sys.stdin:
    line = line.strip().split()
    out = [digits[int(n)] for n in line]
    print(" ".join(out))
