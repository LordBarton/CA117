#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x:.1f}, {self.y:.1f})'

    def midpoint(self, other):
        nx = (self.x + other.x) / 2
        ny = (self.y + other.y) / 2
        return Point(nx, ny)
