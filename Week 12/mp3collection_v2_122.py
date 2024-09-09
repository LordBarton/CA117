#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title=None, duration=None, artists=None):
        if artists == None:
            self.arists = []
        else:
            self.artists = artists
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}\nDuration: {self.duration}"

class MP3Collection(object):

    def __init__(self):
        self.collection = {}

    def add(self, track):
        self.collection[track.title] = track

    def remove(self, title):
        if title in self.collection:
            del self.collection[title]
        else:
            pass

    def lookup(self, title):
        if title in self.collection:
            return self.collection[title]
        else:
            return None

    def __add__(self, other):
        newcoll = MP3Collection()
        newcoll.collection.update(self.collection)
        newcoll.collection.update(other.collection)
        return newcoll

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c1 = MP3Collection()
    c1.add(t1)
    c1.add(t2)

    c2 = MP3Collection()
    c2.add(t3)

    # Make a new collection from two existing ones
    c3 = c1 + c2
    assert(isinstance(c3, MP3Collection))
    assert(c3 is not c1)
    assert(c3 is not c2)

if __name__ == '__main__':
    main()
