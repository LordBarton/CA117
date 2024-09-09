#!/bin/usr/env python3

class Contact(object):

    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'

class Contactlist(object):

    def __init__(self):
        self.d = {}

    def add(self, contact):
        self.d[contact.name] = contact

    def remove(self, name):
        del self.d[name]

    def get(self, name):
        if name in self.d:
            return self.d[name]
        return None

    def __str__(self):
        ls = sorted([n for n in self.d])
        output = 'Contact list\n------------\n'
        for n in ls:
            output += str(self.d[n]) + "\n"
        return output.strip()
