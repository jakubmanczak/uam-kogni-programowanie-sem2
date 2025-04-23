# Średnia arytmetyczna: Napisz funkcję srednia(lista), która oblicza średnią arytmetyczną elementów w danej liście.
# Przykład użycia: srednia([10, 20, 30, 40]) powinno zwrócić 25.0.

def srednia(lista):
    suma = 0
    for liczba in lista:
        suma += liczba
    return suma/len(lista)

assert(srednia([10, 20, 30, 40]) == 25.0)
print(srednia([10, 20, 30, 40]))
