#!/usr/bin/env python3

import sys
import calendar

lines = sys.stdin.readlines()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
poem = ["is fair of face", "is full of grace", "is full of woe", "has far to go", "is loving and giving", "works hard for a living", "is fair and wise and good in every way"]
for s in lines:
    s = s.strip().split()
    day = int(s[0])
    month = int(s[1])
    year = int(s[2])
    num = calendar.weekday(year, month, day)
    print(f'You were born on a {days[num]} and {days[num]}\'s child {poem[num]}.')
