#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for s in lines:
    s = s.strip().lower()
    spl = s.split()
    if spl[0] in spl[1]:
        print("True")
    else:
        print("False")
