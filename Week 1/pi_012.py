#!/usr/bin/env python3

import sys
from math import pi
n = sys.stdin.readlines()

for i in n:
    i = int(i.strip())
    print(f'{pi:.{i}f}')
