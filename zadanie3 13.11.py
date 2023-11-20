# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:43:09 2023

@author: student
"""

class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        
    def __str__(self):
        return f"Property: {self.address}\nArea: {self.area} metry kwadratowe\nRooms: {self.rooms}\nPrice: {self.price} zl"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House:\n{super().__str__()}\nPlot Size: {self.plot} sq. meters"



class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat:\n{super().__str__()}\nFloor: {self.floor}"


dom = House(area=150, rooms=4, price=300000, address="123 ul. abc", plot=500)
mieszkanie = Flat(area=80, rooms=2, price=150000, address="456 ul. cba", floor=3)


print(dom,"\n----------------------\n",mieszkanie)









