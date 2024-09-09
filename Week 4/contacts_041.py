#!/usr/bin/env python3

import sys

f = open(sys.argv[1], 'r')
content = f.readlines()
contact = {}

for line in content:
    line = line.strip().split()
    contact[line[0]] = line[1]

input = sys.stdin.readlines()

for s in input:
    s = s.strip()
    if s in contact.keys():
        print(f'Name: {s}\nPhone: {contact[s]}')
    else:
        print(f'Name: {s}\nNo such contact')
