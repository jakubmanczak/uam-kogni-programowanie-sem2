# zadanie 7
lista = []
for i in range(50):
    lista.append(0)

for i in range(len(lista)):
    if i % 2 == 0:
        lista[i] = 2
    if i % 3 == 0:
        lista[i] = 3
    if i % 5 == 0:
        lista[i] = 5

for liczba in lista[:]:
    if liczba == 0:
        lista.remove(0)

lista.sort()

print(f"Lista ma {len(lista)} elementów.")
