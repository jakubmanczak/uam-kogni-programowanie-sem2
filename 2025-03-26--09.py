# zadanie 10
import random

print("Jak dużo liczb wygenerować?")
liczba = int(input())

print("+---+------+")
for i in range(liczba):
    los = random.random()
    los = round(los, 2)
    if len(str(los)) == 3:
        los = str(los) + "0"
        print(f"| {i} | {los} |")
    else:
        print(f"| {i} | {los:.2} |")
print("+---+------+")
