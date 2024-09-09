#!/usr/bin/env python3

def collatz(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 0:
        return collatz(n // 2)
    return collatz(n * 3 + 1)
