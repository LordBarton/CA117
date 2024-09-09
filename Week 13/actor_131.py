#!/usr/bin/env python3

class Actor(object):

    def __init__(self, name, nationality, fee):
        self.name = name
        self.nationality = nationality
        self.fee = fee

    def __str__(self):
        return f'Name: {self.name}\nNationality: {self.nationality}\nFee: {self.fee}'
