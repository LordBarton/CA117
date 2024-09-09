#!/usr/bin/env python3

import sys

N = [int(n) for n in list(sys.stdin.readline().strip()) if n != '0']
total = 9
while total > 8:
    temp = 1
    for n in N:
        temp *= n
    total = temp
    N = [int(m) for m in list(str(total)) if m != '0']
print(N[0])
