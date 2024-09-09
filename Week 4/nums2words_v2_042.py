#!/usr/bin/env python3

import sys

my_dict = {
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

def num2word(n):
    if n not in my_dict:
        return("unknown")
    return(my_dict[n])

for lines in sys.stdin:
    lines = lines.strip().split()
    out = [num2word(int(n)) for n in lines]
    print(" ".join(out))
