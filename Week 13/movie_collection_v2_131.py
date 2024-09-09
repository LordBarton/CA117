#!/usr/bin/env python3

class Actor(object):

    def __init__(self, name, nationality, fee):
        self.name = name
        self.nationality = nationality
        self.fee = fee

    def __str__(self):
        return f'Name: {self.name}\nNationality: {self.nationality}\nFee: {self.fee}'

class Movie(object):

    def __init__(self, title, duration, cast=None):
        self.title = title
        self.duration = duration
        if cast is None:
            self.cast = {}

    def add(self, actor):
        if actor.name not in self.cast:
            self.cast[actor.name] = actor

    def remove(self, name):
        if name in self.cast:
            del self.cast[name]

    def lookup(self, name):
        if name in self.cast:
            return self.cast[name]

class MovieCollection(object):

    def __init__(self):
        self.collection = []

    def add(self, movie):
        if movie not in self.collection:
            self.collection.append(movie)

    def __str__(self):
        L = len(self.collection)
        dur = 0
        for movie in self.collection:
            dur += movie.duration
        durh = dur // 60
        durm = dur % 60

        actorz = {}
        for movie in self.collection:
            for actor in movie.cast:
                if actor not in actorz:
                    actorz[actor] = ""
        acc = len(actorz)
        return f'Movies: {L}\nActors: {acc}\nDuration: {durh} hour(s) {durm:02d} minute(s)'
