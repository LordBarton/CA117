#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name=None, tid=None):
        self.name = name
        self.tid = tid

    def __str__(self):
        return f"Name: {self.name}\nID: {self.tid}"

class Triathlon(object):

    def __init__(self):
        self.collection = {}

    def add(self, athlete):
        self.collection[athlete.tid] = athlete.name

    def remove(self, num):
        del self.collection[num]

    def lookup(self, num):
        if num in self.collection:
            return Triathlete(self.collection[num], num)
        else:
            return None

    def __str__(self):
        newcoll = dict(sorted(self.collection.items(), key=lambda item: item[1]))
        output = ""
        for s in newcoll.items():
            inst = Triathlete(s[1], s[0])
            output += str(inst) + "\n"
        return output.strip()

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
