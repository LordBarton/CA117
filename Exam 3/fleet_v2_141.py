#!/usr/bin/env python3

class Vehicle(object):

    def __init__(self, reg, cat, mileage, drivers=None):
        self.reg = reg
        self.cat = cat
        self.mileage = mileage
        if drivers is None:
            self.drivers = []
        else:
            self.drivers = drivers

    def __str__(self):
        return f'Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {", ".join(self.drivers)}'

class Fleet(object):

    def __init__(self):
        self.fleet = {}

    def add(self, car):
        if car.reg not in self.fleet:
            self.fleet[car.reg] = car

    def remove(self, car):
        if car in self.fleet:
            del self.fleet[car]

    def lookup(self, regis):
        if regis in self.fleet:
            return self.fleet[regis]

    def get_drivers_by_category(self, n):
        auth = {}
        for car in self.fleet.values():
            if car.cat == n:
                for d in car.drivers:
                    if d not in auth:
                        auth[d] = ""
        out = []
        for k in auth.keys():
            out.append(k)
        return out
