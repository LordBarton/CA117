#!/usr/bin/env python3

class Student(object):

    def __init__(self, name=None, id=None, mods=None):

        self.name = name
        self.id = id
        self.mods = mods

    def __str__(self):

        mods = sorted([s[0] for s in self.mods])
        grades = [s[1] for s in self.mods]
        total = 0
        for n in grades:
            total += int(n)
        avg = round(total / len(grades))

        return f'Name: {self.name}\nID: {self.id}\nModules: {", ".join(mods)}\nAverage mark: {avg}'

class Classlist(object):

    def __init__(self):
        self.d = {}

    def add(self, student):
        avg = (str(student).split("\n")[3])
        avg = avg[-2:]
        self.d[str(student)] = avg

    def __str__(self):
        sortd = sorted(self.d)
        output = ""
        for s in sortd:
            output += s + "\n"
        return output.strip()
