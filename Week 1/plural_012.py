#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
es1 = ["ch", "sh"]
es2 = ["x", "s", "z", "o"]
vowels = ["a", "i", "e", "o", "u", "y"]
for line in lines:
    line = line.strip()

    if line[-2:] in es1:
        print(line + "es")
    elif line[-2] not in vowels and line[-1] == "y":
        print(line[:-1] + "ies")
    elif line[-1] == "f":
        print(line[:-1] + "ves")
    elif line[-2:] == "fe":
        print(line[:-2] + "ves")
    elif line[-1] in es2:
        print(line + "es")
    else:
        print(line + "s")
