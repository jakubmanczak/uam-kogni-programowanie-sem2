# zadanie 4
import random

cyfry = []
for i in range(100):
    cyfry.append(random.randint(0, 9))

liczba_siodemek = 0
for cyfra in cyfry:
    if cyfra == 7:
        liczba_siodemek += 1
print(f"Liczba 7 pojawiła się w liście {liczba_siodemek} razy.")
