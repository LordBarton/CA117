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
        self.movie = {}
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
