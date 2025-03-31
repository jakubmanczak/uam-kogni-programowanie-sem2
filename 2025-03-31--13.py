import os

ksiazka = { "jmanczak": "pierwszy", "madejczyk": "jak stąd wyjść", "chalkeater": "pomocy" }
while True:
    print("Witaj w hotelu California. Oto księga gości.")
    print("Co chcesz z nią zrobić?\n(p) przeczytać,\n(w) wpisać się,\n(u) usunąć kogoś,\n(z) zmienić wpis,\n(q) wyjść z hotelu California.")
    print("Twój wybór: ", end="")
    wybor = input()
    print("---------------------------")
    if wybor == "p":
        print(ksiazka)
    elif wybor == "w":
        print("Pod jaką nazwą chcesz się wpisać? Podaj: ", end="")
        nazwa = input()
        if nazwa in ksiazka:
            print("Ej, ale jest już ktoś taki. Wybierz opcję (z) zmienić wpis.")
        else:
            print("Co chcesz tam wpisać? Podaj: ", end="")
            wpis = input()
            ksiazka[nazwa] = wpis
    elif wybor == "u":
        print("Kogo usunąć? Podaj: ", end="")
        do_kosza = input()
        if do_kosza in ksiazka:
            del(ksiazka[do_kosza])
        else:
            print("Nie ma tam takiej osoby...")
    elif wybor == "z":
        print("Czyj wpis zmienić? Podaj: ", end="")
        nazwa = input()
        if nazwa in ksiazka:
            print("Co wpisać pod tą nazwą? Podaj: ", end="")
            wpis = input()
            ksiazka[nazwa] = wpis
        else:
            print("Jak zmienić wpis kogoś, kogo tam nie ma??")
    elif wybor == "q":
        print("Nie można wyjść z hotelu California... No dobra, Tobie pozwolę.")
        break
    else:
        print("Nieprawidłowa opcja.")
    print("------------------------------------")
    print("Wpisz cokolwiek aby wyczyścić ekran.")
    input()
    os.system("clear")
