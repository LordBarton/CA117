#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

def replace_t(n):
    n = int(n)
    ran = range(1, n + 1)
    return [0 if m % 3 else m for m in ran]

for n in s:
    print(f'Non-multiples of 3 replaced: {replace_t(n)}')
