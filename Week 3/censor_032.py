#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
file = sys.argv[1]

def censor(lst):
    words = []
    for s in lines:
        words.append(s.strip())
    f = open(file, 'r')
    content = f.read().strip()
    out = " "
    for n in content:
        for w in words:
            if w in n.lower():
                n = n.replace(w, "@" * len(w))
        out += n
    print(out)
censor(lines)
