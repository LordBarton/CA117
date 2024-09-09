#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

list1 = []
list2 = []

i = 0
while i < len(input):
    if i % 2 == 0:
        list1.append(input[i])
    else:
        list2.append(input[i])
    i += 1

list2 = sorted(list2, key=len, reverse=True)

for n in list1:
    print (n)
for n in list2:
    print (n)
