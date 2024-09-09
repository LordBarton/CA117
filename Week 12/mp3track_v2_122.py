#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title=None, duration=None, artists=None):
        if artists == None:
            self.artists = []
        else:
            self.artists = artists
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}\nBy: {', '.join(self.artists)}\nDuration: {self.duration}"

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    print(t1)
    print(t2)
    print(t3)

if __name__ == '__main__':
    main()
