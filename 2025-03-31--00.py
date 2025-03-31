#
# .append -> [[]]
# .extend -> [...]
#

wyniki = [["Adam", 21, 1000], ["Kasia", 37, 3], ["Piotr", 45, 2345], ["Agata", 90, 687]]
# print(wyniki[0])
# for wiersz in wyniki:
#     for kolumna in wiersz:
#         # print(kolumna, end=" ")
#         print(kolumna, end="\t")
#     print()

# slownik={
#     1: "jeden",
#     2: "dwa",
#     3: "trzy",
#     4: "cztery"
# }
# print(slownik[1])
# print(slownik)

slownik = {
    "jeden": "one",
    "dwa": "two",
    "trzy": "three",
    "cztery": "four"
}
# print("Podaj nowe hasło: ", end="")
# haslo = input()
# print("Podaj definicję nowego hasła: ", end="")
# definicja = input()
# slownik[haslo] = definicja
# print(slownik)

# if "dwa" in slownik:
#     print("Dopadłem go!")
# else:
#     print("Nie będzie dzisiaj obiadu.")

# print(slownik)
# print("Wpisz hasło do usunięcia: ", end="")
# input = input()
# del(slownik[input])
# print(slownik)

# print(slownik.keys())
# print(slownik.values())

# set1 = {1,2,3,1,2,3}
#      ^ this gets immediately cut down to {1,2,3}
# set2 = set([1,2,3,4,5])
# print(set1)
# print(len(set1))
# print(set2)

# lista = [1,2,3,4,3,3]
# lista = list(set(lista))
#         ^ cuts out duplicates
# print(lista) # [1,2,3,4]


# set1 = {1,2,3,4,5}
# set1.add(6)
# print(set1)
# set1.remove(6)
# #    ^ deletes value from set, errors if not present
# set1.discard(6)
# #    ^ deletes value from set, silent if not present
# print(set1)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.difference(set2).union(set2.difference(set1)))
