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

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
