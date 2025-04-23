# Lista bez powtórzeń: Napisz funkcję, która zwraca listę wylosowanych bez powtórzeń parzystych liczb.
# Funkcja pobiera liczbę elementów do wylosowania. Nie używaj setów.
# Zaprezentuj działanie funkcji dla trzechrożnych argumentów wejściowych.

import random

def bez_powtorzen(liczba):
    lista = []
    for i in range(liczba):
        while True:
            los = random.randint(1, 99)
            if not(los in lista) and (los % 2 == 0):
                lista.append(los)
                break
    return lista

print(bez_powtorzen(2))
print(bez_powtorzen(7))
print(bez_powtorzen(15))
