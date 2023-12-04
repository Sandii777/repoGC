# a


def wyswietl_imiona(imiona):
    for imie in imiona:
        print(imie)


lista_imion = ["Anna", "Bartek", "Cezary", "Dorota", "Eryk"]


wyswietl_imiona(lista_imion)

# b1


def pomnoz_przez_dwa_for(liczby):
    wyniki = []
    for liczba in liczby:
        wyniki.append(liczba * 2)
    return wyniki


lista_liczb_for = [1, 2, 3, 4, 5]


wyniki_for = pomnoz_przez_dwa_for(lista_liczb_for)
print(wyniki_for)

# b2


def pomnoz_przez_dwa_skrot(liczby):
    return [liczba * 2 for liczba in liczby]


lista_liczb_skrot = [1, 2, 3, 4, 5]

wyniki_skrot = pomnoz_przez_dwa_skrot(lista_liczb_skrot)
print(wyniki_skrot)

# c


def wyswietl_parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


lista_liczb = list(range(1, 21))

wyswietl_parzyste(lista_liczb)

# d


def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


lista_liczb = list(range(1, 21))

wyswietl_co_drugi(lista_liczb)
