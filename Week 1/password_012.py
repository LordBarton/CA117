#!/usr/bin/env python3

import sys

psw = sys.stdin.readlines()
for line in psw:
    c1, c2, c3, c4 = 0, 0, 0, 0
    line = line.strip()
    for w in line:
        if w >= "a" and w <= "z":
            c1 = 1
        elif w >= "A" and w <= "Z":
            c2 = 1
        elif w >= "0" and w <= "9":
            c3 = 1
        else:
            c4 = 1
    print(c1 + c2 + c3 + c4)
