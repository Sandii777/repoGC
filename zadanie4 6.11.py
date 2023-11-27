# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:30:05 2023

@author: sandr
"""


def sprawdz(liczba: int, liczba2: int, liczba3: int) -> bool:
    return liczba + liczba2 >= liczba3


wynik4 = sprawdz(1, 4, 6)
if wynik4 is True:
    print("Prawda")
else:
    print("Nieprawda")
