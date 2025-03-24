print("Podaj pięć liczb (odgradzając enterami): ")
liczba1 = int(input())
liczba2 = int(input())
liczba3 = int(input())
liczba4 = int(input())
liczba5 = int(input())

maxliczba = 0
indeks = 0
if liczba1 >= maxliczba:
    maxliczba = liczba1
    indeks = 1
if liczba2 > maxliczba:
    maxliczba = liczba2
    indeks = 2
if liczba3 > maxliczba:
    maxliczba = liczba3
    indeks = 3
if liczba4 > maxliczba:
    maxliczba = liczba4
    indeks = 4
if liczba5 > maxliczba:
    maxliczba = liczba5
    indeks = 5

print(f"Największa była liczba nr. {indeks}, która wynosi {maxliczba}")
