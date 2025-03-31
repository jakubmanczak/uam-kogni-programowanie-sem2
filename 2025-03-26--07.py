# zadanie 8
import random

lista = []
for i in range(20):
    lista.append(random.randint(0, 99))

for liczba in lista[:]:
    if liczba > 50:
        lista.remove(liczba)

print(lista)
print(f"W liście zostało {len(lista)} elementów.")
