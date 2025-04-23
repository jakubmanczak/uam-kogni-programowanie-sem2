# Suma liczb parzystych: Napisz funkcję suma_parzystych(lista),
# która oblicza sumę wszystkich liczb parzystych w danej liście.
# Przykład użycia: suma_parzystych([1, 2, 3, 4, 5, 6]) powinno zwrócić 12.

def suma_parzystych(lista):
    suma = 0
    for liczba in lista:
        if liczba % 2 == 0:
            suma += liczba
    return suma

assert(suma_parzystych([1, 2, 3, 4, 5, 6]) == 12)
print(suma_parzystych([1, 2, 3, 4, 5, 6]))
