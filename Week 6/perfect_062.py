#!/usr/bin/env python3

import sys

def get_divisors(n):
    out = []
    for i in range(1,n+1):
        m = n / i
        if m % 1 == 0:
            out.append(i)
    return out

def get_proper_divisors(n):
    out = get_divisors(n)
    out.remove(n)
    return out

def is_perfect(n):
    total = 0
    for m in get_proper_divisors(n):
        total += m
    if total == n:
        return True
    return False
