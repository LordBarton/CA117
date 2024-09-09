#!/usr/bin/env python3

class CashRegister(object):

    def __init__(self, total=0):
        self.total = total
        self.count = 0

    def add_item(self, amount=0):
        self.amount = amount
        self.total += amount
        if amount > 0:
             self.count += 1

    def clear(self):
        self.total = 0
        self.count = 0

    def __str__(self):
        return f'Items: {self.count}\nTotal: {self.total:.2f}'
