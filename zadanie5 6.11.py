# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:31:11 2023

@author: sandr
"""

# ### Zadanie 5

def sprawdz(lista: list, liczba: int) -> bool:
    return liczba in lista

listaa=[1,2,3,4,5,6]

wynik5 = sprawdz(listaa, 10)

if wynik5==True:
    print("Tak")
else:
    print("Nie")
