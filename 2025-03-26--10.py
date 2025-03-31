# zadanie 11
imiona = ["Jakub", "Bruno", "Stanisław", "Mateusz"]
zawod = ["Bezrobotny", "IT QA", "IT DevOps", "Bezrobotny"]

print("Jaki zawód wyświetlić? (Bezrobotny, IT QA, IT DevOps)")
wybor = input()

print("Oto przedstawiciele:")
for i in range(len(imiona)):
    if zawod[i] == wybor:
        print(imiona[i])
