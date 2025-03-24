print("Czy chcesz napić się piwa?")
decyzja_piwo = input()
# decyzja_piwo = input().lower()
# ^^ tak mi jeszcze nie wolno

if decyzja_piwo == "tak" or decyzja_piwo == "Tak" or decyzja_piwo == "TAK":
    print("Czy masz 18 lub więcej lat?")
    potwierdzenie_wieku = input()
    if potwierdzenie_wieku == "tak" or potwierdzenie_wieku == "Tak" or potwierdzenie_wieku == "TAK":
        print("Możesz!")
    else:
        print("Nie możesz!")
else:
    print("No trudno!")
