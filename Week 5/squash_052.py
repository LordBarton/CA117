#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

def count(input):
    for line in input:
        line = list(line)
        out = []
        i = 0
        j = 0
        while i < len(line):
            temp = line[i]
            temp_count = 0
            while i < len(line) and line[i] == temp:
                i += 1
                temp_count += 1
            out.append(str(temp_count) + temp)
        print("".join(out))
count(input)
