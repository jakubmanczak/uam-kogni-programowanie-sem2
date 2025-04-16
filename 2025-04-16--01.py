# zadanie 1
def odejmowanie(x, y):
    return x-y

# zadanie 2
def ostatni(lista):
    return lista[-1]

# zadanie 3
def ogon(lista):
    return lista[1:]

# zadanie 4
def dlugosc(lista):
    dl = 0
    for el in lista:
        dl += 1
    return dl

# zadanie 5
def maksimum(lista):
    # nadal uważam że sztywne ustawienie wartości min/max
    # na taką niemożliwą do spotkania w liście ma swoje plusy
    # ma swoje plusy; chociażby w przypadku pustej listy
    maks = lista[0]
    for el in lista[1:]:
        if el > maks:
            maks = el
    return maks

def minimum(lista):
    # to samo co wyżej
    mini = lista[0]
    for el in lista[1:]:
        if el < mini:
            mini = el
    return mini

# zadanie 6
def nta(lista, nty):
    return lista[nty]

# zadanie 7
def alternatywa(p, q):
    # no ternary :C
    if p == 1 or q == 1:
        return 1
    else:
        return 0

# zadanie 8
def koniunkcja(p, q):
    if p == 1 and q == 1:
        return 1
    else:
        return 0

# zadanie 9
def implikacja(p, q):
    if p == 1 and q == 0:
        return 0
    else:
        return 1

# zadanie 10
def zmniejsz(input):
    duze = "QWERTYUIOPASDFGHJKLZXCVBNM"
    male = "qwertyuiopasdfghjklzxcvbnm"
    output = ""
    for litera in input:
        if litera in duze:
            for i in range(len(duze)):
                if duze[i] == litera:
                    output += male[i]
                    break
        else:
            output += litera
    return output

zdanie = "Dzien Dobry Drogie Dzieci"
print(f"{zmniejsz(zdanie)}")
