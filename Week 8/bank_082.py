#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, dep=0):
        self.dep = dep
        self.balance += self.dep

    def withdraw(self, withdrawal=0):
        self.withdrawal = withdrawal
        if self.balance >= self.withdrawal:
            self.balance -= self.withdrawal

    def __str__(self):
        return 'Your current balance is {:.2f} euro'.format(self.balance)
