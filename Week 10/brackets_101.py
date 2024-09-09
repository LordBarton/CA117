#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(s):
    stack = Stack()
    lefties = "({["
    righties = ")}]"

    for bracket in s:
        if bracket in lefties:
            stack.push(bracket)
        elif bracket in righties:
            if stack.is_empty():
                return False
            top = stack.pop()
            if lefties.index(top) != righties.index(bracket):
                return False

    return stack.is_empty()
