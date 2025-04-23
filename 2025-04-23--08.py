# Zamiana miejscami pierwszego i ostatniego elementu: Napisz funkcję zamien_pierwszy_i_ostatni(lista),
# która zamienia miejscami pierwszy i ostatni element listy.
# Przykład użycia: zamien_pierwszy_i_ostatni([10, 20, 30, 40]) powinno zwrócić [40, 20, 30, 10].

def zamien_pierwszy_i_ostatni(lista):
    if len(lista) < 2:
        return lista
    pierwszy = lista[0]
    ostatni = lista[-1]
    lista[0] = ostatni
    lista[-1] = pierwszy
    return lista

assert(zamien_pierwszy_i_ostatni([10, 20, 30, 40]) == [40, 20, 30, 10])
print(zamien_pierwszy_i_ostatni([10, 20, 30, 40]))
