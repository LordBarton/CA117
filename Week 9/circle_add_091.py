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

class Circle(object):

    def __init__(self, centre=None, radius=1):
        if centre is None:
            centre = Point()
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return f'Centre: {self.centre}\nRadius: {self.radius}'

    def __add__(self, other):
         c = (self.centre.midpoint(other.centre))
         r = (self.radius + other.radius)
         return (Circle(c, r))
