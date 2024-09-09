#!/usr/bin/env python3

import sys

words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety", 100:"one hundred"
}


for line in sys.stdin:
    part = line.strip().split()
    out = []
    for n in part:
        n = int(n)
        if n <= 20 or n == 100:
            out.append(words[n])
        else:
            tens = (n // 10) * 10
            ones = n % 10
            if ones > 0:
                final = words[tens] + "-" + words[ones]
            else:
                final = words[tens]
            out.append(final)
    print(" ".join(out))
