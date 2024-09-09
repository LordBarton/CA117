#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for s in lines:
    s = s.strip().lower()
    ns = ""
    for w in s:
        if w > "a" and w < "z" or (w > "0" and w < "9"):
            ns += w
    rev = ns[::-1]
    if ns == rev:
        print("True")
    else:
        print("False")
