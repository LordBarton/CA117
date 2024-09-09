#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

seen = set()

for line in input:
    output = []
    for s in line.split():
        ss = s.lower().strip(".").strip(",").strip("!").strip("?").strip(":").strip(";")
        if ss not in seen:
            seen.add(ss)
            output.append(s)
        else:
            output.append(".")
    print (" ".join(output))
