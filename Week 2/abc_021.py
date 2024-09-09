#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

stt = lines[0].split()
st = []
for s in stt:
    st.append(int(s))
st.sort()

abc = {}

abc["A"] = st[0]
abc["B"] = st[1]
abc["C"] = st[2]

out = []
nd = lines[1].strip()
for s in nd:
    for key in abc:
        if s == key:
            out.append(str(abc[key]))
print(" ".join(out))
