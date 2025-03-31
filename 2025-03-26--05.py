# zadanie 6
print("Ile cyfr pobrać?")
ilosc_cyfr = int(input())
cyfry = []
for i in range(ilosc_cyfr):
    cyfry.append(int(input()))

for cyfra in cyfry:
    if cyfra % 2 == 0:
        print(f"Cyfra {cyfra} jest parzysta.")
    else:
        print(f"Cyfra {cyfra} jest nieparzysta.")
