# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:29:37 2023

@author: sandr
"""


def sprawdz(liczba: int) -> bool:
    return liczba % 2 == 0


wynik3 = sprawdz(21)
if wynik3 is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
