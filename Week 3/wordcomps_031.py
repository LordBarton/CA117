#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

def category(list):
    list0 = [s.strip() for s in list]

    list1 = [s for s in list0 if len(s) == 17]
    print(f'Words containing 17 letters: {list1}')

    list2 = [s for s in list0 if len(s) >= 18]
    print(f'Words containing 18+ letters: {list2}')

    list3 = []
    for s in list0:
        count = 0
        for i in s.lower():
            if i == 'a':
                count += 1
        if count == 4:
            list3.append(s)
    print(f'Words with 4 a\'s: {list3}')

    list4 = []
    for s in list0:
        count = 0
        for i in s.lower():
            if i == 'q':
                count += 1
        if count >= 2:
            list4.append(s)
    print(f'Words with 2+ q\'s: {list4}')

    list5 = [s for s in list0 if 'cie' in s]
    print(f'Words containing cie: {list5}')

    list6 = []
    angle = sorted("angle")
    for s in list0:
        if s.lower() != "angle" and sorted(s.lower()) == angle:
            list6.append(s)
    print(f'Anagrams of angle: {list6}')

    return list1, list2, list3, list4, list5, list6

category(lines)
