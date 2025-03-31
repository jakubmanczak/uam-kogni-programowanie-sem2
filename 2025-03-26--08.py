# zadanie 9
import random

lista = []
for i in range(20):
    lista.append(random.randint(0, 99))

# .min() .max() .avg() pls :sob:
min = 100
max = -1
avg = 0
for liczba in lista:
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba
    avg += liczba
avg /= len(lista)

print(f"Najmniejsza: {min}")
print(f"Największa: {max}")
print(f"Średnia: {avg}")
