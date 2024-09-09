#!/usr/bin/env python3

import sys
lines = []
lineslower = []

def binsearch (query, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False

for line in sys.stdin:
    lines.append(line.strip())
    lineslower.append(line.lower().strip())
print([word for word in lines if binsearch (word.lower()[::-1], lineslower) and len(word) >= 5])
