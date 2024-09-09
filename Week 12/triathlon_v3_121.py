#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name=None, tid=None):
        self.name = name
        self.tid = tid
        self.dict = {}
        self.total = 0

    def __str__(self):
        return f"Name: {self.name}\nID: {self.tid}\nRace time: {self.total}"

    def add_time(self, disc=None, time=None):
        self.dict[disc] = time
        self.total += time

    def get_time(self, var):
        return self.dict[var]

    def __eq__(self, other):
        return self.total == other.total

    def __lt__(self, other):
        return self.total < other.total

    def __gt__(self, other):
        return self.total > other.total

class Triathlon(object):

    def __init__(self):
        self.collection = {}

    def add(self, athlete):
        self.collection[athlete.tid] = athlete

    def remove(self, num):
        del self.collection[num]

    def lookup(self, num):
        if num in self.collection:
            return Triathlete(self.collection[num], num)
        else:
            return None
    def best(self):
        best = None
        for s in self.collection.values():
            if best is None:
                best = s
            elif best > s:
                best = s
        return best

    def worst(self):
        worst = None
        for s in self.collection.values():
            if worst is None:
                worst = s
            elif worst < s:
                worst = s
        return worst

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
