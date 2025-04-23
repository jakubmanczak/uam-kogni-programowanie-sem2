# Usuwanie duplikatów: Napisz funkcję usun_duplikaty(lista), która usuwa powtarzające się elementy z listy.
# Nie używaj setów. Przykład użycia: usun_duplikaty([1, 2, 2, 3, 3, 4]) powinno zwrócić [1, 2, 3, 4].

# To jest rozwiązanie alternatywne do proponowanego podczas zajęć:
# wg. prowadzącego lepiej jest utworzyć nową listę i dodawać
# do niej elementy, których w niej jeszcze nie ma.
def usun_duplikaty(lista):
    wystapienia = {}
    for element in lista:
        if element in wystapienia:
            wystapienia[element] += 1
        else:
            wystapienia[element] = 1
    for element in lista:
        liczba_wyst = wystapienia[element]
        for i in range(liczba_wyst - 1):
            lista.remove(element)
    return lista

assert(usun_duplikaty([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4])
print(usun_duplikaty([1, 2, 2, 3, 3, 4]))
