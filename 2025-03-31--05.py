print("Podaj ile elementów chcesz wpisać: ", end="")
ilosc = int(input())

elementy = []
for i in range(ilosc):
    print(f"Podaj element (i{i}): ", end="")
    elementy.append(input())

wystapienia = {}
for el in elementy:
    if el in wystapienia:
        wystapienia[el] += 1
    else:
        wystapienia[el] = 1

print(wystapienia)
