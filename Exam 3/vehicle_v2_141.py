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

    def add_driver(self, driver):
        if driver not in self.drivers:
            self.drivers.append(driver)

    def __str__(self):
        return f'Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {", ".join(self.drivers)}'

