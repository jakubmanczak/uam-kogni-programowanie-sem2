# typy tablicowe cz. 1

# lista_cyfr_trzy = [3, "III", "trzy", "three", "..."]
# lista_pusta = [] # wartość logiczna listy
# indeksowanie jako odległość od początku listy
# dlugosc_listy = len(lista_cyfr_trzy)

# print("Elementy listy:")
# for i in range(len(lista_cyfr_trzy)):
#     print(f"i{i}: {lista_cyfr_trzy[i]}")

# hardcoding leads to point loss

# for cyfra in lista_cyfr_trzy:
#     print(cyfra)

# zakresy -> lower bound inclusive, outer bound exclusive
# print(lista_cyfr_trzy)
# print(lista_cyfr_trzy[1:2])
# print(lista_cyfr_trzy[1:])
# print(lista_cyfr_trzy[:3])

# lista = [1,2,3]
# print(lista)
# print("Podaj wartość do zastąpienia elementu i0")
# lista[0] = int(input())
# print(lista)

# for i in range(len(lista)):
#     print(f"Podaj nową zawartość i0 (aktualnie {lista[i]})")
#     lista[i] = input()
# print(lista)

# print(lista)
# for i in range(2):
#     print("Dodaj element do listy")
#     lista.append(int(input()))
# print(lista)

# print("Podaj liczbe do usuniecia")
# lista.remove(int(input()))
# print(lista)

# deep copy & shallow copy
# lista1 = [1,2,3,4]
# lista2 = lista1
# lista1[0] = 8
# print(lista1)
# print(lista2)

# print("----")
# lista1 = [1,2,3,4]
# lista2 = lista1[:]
# lista1[0] = 8
# print(lista1)
# print(lista2)

# print("----")
# lista = [1,2,3,2,3,4,2]
# print(lista)
# for liczba in lista[:]:
#     if liczba == 2:
#         lista.remove(liczba)
# print(lista)

# owoce = ["jabłko", "banan", "gruszka"]
# usuniety = owoce.pop(1)
# print(usuniety)
# print(owoce)

kolejnosc = [123, 5635463546, 1, 5, 78, 111]
print(kolejnosc)
kolejnosc.sort()
print(kolejnosc)
kolejnosc.sort(reverse=True)
print(kolejnosc)
