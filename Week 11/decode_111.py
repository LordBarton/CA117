#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

vowels = "aieou"

for line in input:
    output = ""
    i = 0
    while i < len(line):
        output += line[i]
        if line[i] in vowels:
            i += 2
        i += 1
    print (output)

