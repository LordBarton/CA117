#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

max_name = 0
for s in lines:
    s = s.strip().split()
    club = " ".join(s[1:-8])
    if len(club) > max_name:
        max_name = len(club)
CLUB = "CLUB" + (max_name - 2) * " "
P = "P" + 3 * " "
W = "W" + 3 * " "
D = "D" + 3 * " "
L = "L" + 2 * " "
GF = "GF" + 2 * " "
GA = "GA" + 2 * " "
GD = "GD" + " "
PTS = "PTS"
print("POS", CLUB + P + W + D + L + GF + GA + GD + PTS)
for s in lines:
    s = s.strip().split()
    pos = int(s[0])
    club = " ".join(s[1:-8])
    P = int(s[-8])
    W = int(s[-7])
    D = int(s[-6])
    L = int(s[-5])
    GF = int(s[-4])
    GA = int(s[-3])
    GD = int(s[-2])
    PTS = int(s[-1])
    print(f'{pos:3d} {club:{max_name}s} {P:2d} {W:3d} {D:3d} {L:3d} {GF:3d} {GA:3d} {GD:3d} {PTS:3d}')
