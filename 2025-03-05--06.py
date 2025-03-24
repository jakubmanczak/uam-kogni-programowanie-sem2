print("Podaj pierwszą liczbę: ")
liczba1 = float(input())
print("Podaj drugą liczbę: ")
liczba2 = float(input())

print("Wpisz jaką operację wykonać na powyższych liczbach (+; -; *; /; %; **): ")
operacja = input()

if operacja == "+" or operacja == "dodawanie":
    wynik = liczba1 = liczba2
    print(f"Wynik operacji {liczba1}+{liczba2}: {wynik}")
elif operacja == "-" or operacja == "odejmowanie":
    wynik = liczba1 - liczba2
    print(f"Wynik operacji {liczba1}-{liczba2}: {wynik}")
elif operacja == "*" or operacja == "mnożenie":
    wynik = liczba1 * liczba2
    print(f"Wynik operacji {liczba1}*{liczba2}: {wynik}")
elif operacja == "/" or operacja == "dzielenie":
    wynik = liczba1 / liczba2
    print(f"Wynik operacji {liczba1}/{liczba2}: {wynik}")
elif operacja == "%" or operacja == "modulo":
    wynik = liczba1 % liczba2
    print(f"Wynik operacji {liczba1}%{liczba2}: {wynik}")
elif operacja == "**" or operacja == "potęgowanie":
    wynik = liczba1 ** liczba2
    print(f"Wynik operacji {liczba1}**{liczba2}: {wynik}")
else:
    print("Nieprawidłowy operator!")
