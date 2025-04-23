# Zamiana cyfr na ich kwadraty: Napisz funkcję cyfry_na_kwadraty(liczba),
# która zamienia cyfry w podanej liczbie na ich kwadraty.
# Przykład użycia: cyfry_na_kwadraty(123) powinno zwrócić 149.

# Z uwagi na brak informacji co robić w przypadku cyfr większych od 3,
# a więc produkujących kwadrat nie mieszczący się w jednej cyfrze,
# wybrałem zrobić z tego dwie cyfry
# ~ jmanczak
def cyfry_na_kwadraty(liczba):
    lista_cyfr = []
    while liczba != 0:
        if liczba % 10 == 0:
            lista_cyfr.insert(0, 0)
        else:
            lista_cyfr.insert(0, liczba % 10)
        liczba = int(liczba / 10) # liczba = liczba // 10 <- czy tak w ogóle można?
    nowa_liczba = 0
    for liczba in lista_cyfr:
        kwadrat = liczba**2
        if kwadrat >= 10:
            nowa_liczba *= 100
        else:
            nowa_liczba *= 10
        nowa_liczba += kwadrat
    return nowa_liczba

assert(cyfry_na_kwadraty(123) == 149)
print(f"123 -> {cyfry_na_kwadraty(123)}")
print(f"124 -> {cyfry_na_kwadraty(124)}")
print(f"142 -> {cyfry_na_kwadraty(142)}")
