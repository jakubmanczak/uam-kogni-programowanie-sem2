# zadanie 12
imiona = ["Jakub", "Bruno", "Stanisław", "Mateusz"]
zarobki = ["0zl", "9999zl", "7999zl", "0zl"]

while True:
    print("Oto aktualna lista zarobków:")
    for i in range(len(imiona)):
        print(f"{imiona[i]}\t\t{zarobki[i]}")
    print("Co robić dalej? Wyjść (q), Dodać osobę (d)?")
    wybor = input()
    if wybor == "q":
        print("Na razie!")
        break
    elif wybor == "d":
        print("Podaj imie nowej osoby")
        imie = input()
        print("Podaj zarobki nowej osoby (format: liczba+zl)")
        zarobek = input()
        imiona.append(imie)
        zarobki.append(zarobek)
    else:
        print("Nie ma takiej opcji.")
    print("----------------")
