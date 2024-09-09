#!/usr/bin/env python3

import sys

input = [s.strip() for s in sys.stdin.readlines()]

def speed(input):
    start = input[0].split()
    st,sd = int(start[0]),int(start[1])
    speeds = []
    for line in input[1:]:
        line = line.split()
        time, distance = int(line[0]), int(line[1])
        speed = (distance - sd) // (time - st)
        speeds.append(speed)
        st,sd = time,distance
    return max(speeds)

print(speed(input))
