#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]
N = int(input[0])
log = input[1:]

def club(N, log):
    denied, currently = 0, 0
    for line in log:
        line = line.split()
        ppl = int(line[1])
        if line[0] == 'enter':
            if currently + ppl > N:
                denied = denied + 1
            else:
                currently += ppl
        else:
            currently -= ppl
    return denied

print(club(N, log))
