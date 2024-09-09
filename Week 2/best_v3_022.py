#!/usr/bin/env python3

import sys
try:
    f = open(sys.argv[1], 'r')

    max_score = 0
    best = ""

    for line in f:
        try:
            line = line.strip().split()
            score = int(line[0])
            name = " ".join(line[1:])
            if score > max_score:
                max_score = score
                best = name
        except ValueError:
            print(f'Invalid mark {line[0]} encountered. Skipping.')

    print(f'Best student: {best}\nBest mark: {max_score}')

    f.close()


except FileNotFoundError:
    print(f'The file {sys.argv[1]} could not be opened.')


