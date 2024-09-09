#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

def qnou(s):
    s = s.replace("qu", "")
    return "q" in s

out = [word.strip() for word in lines if qnou(word.lower())]

print("Words with q but no u:", out)
