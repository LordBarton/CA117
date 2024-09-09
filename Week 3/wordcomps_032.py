#!/usr/bin/env python3

import sys

dict = sys.stdin.readlines()

def main(lst):
    list = [s.strip() for s in lst]

    vowels = 'aeiuo'
    list1 = []
    for s in list:
        i = 0
        for char in vowels:
            if char in s.lower():
                i += 1
        if i == 5:
            list1.append(s)
    if list1:
        out1 = min(list1, key = len)
    else:
        out1 = None
    print(f'Shortest word containing all vowels: {out1}')

    list2 = [s for s in list if s[-4:] == 'iary']
    print(f'Words ending in iary: {len(list2)}')

    most_e = 0
    out2 = []
    for s in list:
        e_count = 0
        for char in s.lower():
            if char == 'e':
                e_count += 1
        if e_count > most_e:
            most_e = e_count
            out2 = [s]
        elif e_count == most_e:
            out2.append(s)

    print(f'Words with most e\'s: {out2}')

main(dict)
