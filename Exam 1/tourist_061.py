#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]
def tagger(item):
    return item[1]

def visit(input):
    N = int(input[0])
    last = input[-1].split()

    c = last[0]
    kth = int(last[1])
    countries = []
    years = []
    seen = []

    for line in input[1:-1]:
        line = line.split()
        countries.append(line[0])
        years.append(line[1])

    countries = list(zip(countries, years))
    times = 0
    for co,ye in sorted(countries, key=tagger):
        if co == c:
            times += 1
            if times == kth:
                return ye
                break
print(visit(input))
