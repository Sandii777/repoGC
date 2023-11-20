# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:50:21 2023

@author: student
"""

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    def is_passed(self) -> bool:
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50
    
stud1 = Student("Jan Nowak", [60,70,80])
stud2 = Student("Anna Nowak",[40,30,20])

wynik1 = stud1.is_passed()
wynik2 = stud2.is_passed()

print(f"{stud1.name}, passed: {wynik1}")
print(f"{stud2.name}, passed: {wynik2}")