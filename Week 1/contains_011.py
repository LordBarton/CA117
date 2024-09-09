#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for s in lines:
    s = s.strip().lower()
    spl = s.split()
    a = spl[0]
    b = spl[1]
    c = []
    d = []
    e = []
    for w in a:
        c.append(w)
    for w in b:
        d.append(w)
    for w in c:
        if w in d and w not in e:
            e.append(w)
    if c == e:
        print("True")
    else:
        print("False")
