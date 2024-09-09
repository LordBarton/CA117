#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

def prime(n):
    n = int(n)
    ran = range(2, n + 1)
    cons = [2, 3, 5, 7]
    return [m for m in ran if (m in cons) or (m % 2 and m % 3 and m % 5 and m % 7)]
for n in s:
    print(f'Primes: {prime(n)}')
