# zadanie 5
import random

cyfry = []
for i in range(100):
    cyfry.append(random.randint(0, 9))

cyfry.sort()
odwrocone = cyfry[:]
odwrocone.sort(reverse=True)
# odwrocone.reverse() # <- czy tak wolno? chyba nie XD

print(cyfry)
print(odwrocone)
