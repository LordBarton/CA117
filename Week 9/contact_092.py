#!/bin/usr/env python3

class Contact(object):

    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'
