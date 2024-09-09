#!/usr/bin/env python3

import sys

inp = [s.strip() for s in sys.stdin.readlines()]

fst = inp[0].split()

M = int(fst[0])
N = int(fst[1])

seq = inp[1]

count = [str(i) for i in range(M, N + 1)]

out = ""
for n in count:
    out += n

if out == seq:
    print (None)
else:
    i = 0
    while i < len(seq) and seq[i] == out[i]:
        i += 1
    print (out[i])
