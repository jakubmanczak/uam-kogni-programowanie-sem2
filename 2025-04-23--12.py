# Najczęściej występujący element w liście: Napisz funkcję najczestszy_element(lista),
# która zwraca element, który występuje najczęściej w danej liście.
# Przykład użycia: najczestszy_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) powinno zwrócić 4.

def najczestszy_element(lista):
    wystapienia = {}
    for element in lista:
        if element in wystapienia:
            wystapienia[element] += 1
        else:
            wystapienia[element] = 1

    najw = lista[0] # 'dict_keys' object is not subscriptable bla bla bla, najgorzej :C
    for key in wystapienia.keys():
        if wystapienia[key] > najw:
            najw = key
    return najw


assert(najczestszy_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4)
print(najczestszy_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
