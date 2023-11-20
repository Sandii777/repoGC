# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:32:21 2023

@author: sandr
"""

### Zadanie 6

listaa=[1,2,3,4,5]
listaa2=[1,2,6,8,9]

def sprawdz(lista: list, lista2: list) -> list:
    lista3 = lista + lista2 
    lista4 = list(set(lista3))
    lista4 = [x**3 for x in lista4]
    print (lista4)


sprawdz(listaa, listaa2)
