import os

# while True:
#     print("Aby zakończyć program, wpisz \"q\".")
#     print("Aby wyświetlić imię autora, wpisz \"i\".")
#     print("Aby wyświetlić nazwę przedmiotu i kierunek, wpisz \"n\".")
#     print("Aby wyświetlić coś innego, wpisz \"c\".")
#     znak = input()
#     if znak == "q":
#         break
#     elif znak == "i":
#         # os.system("clear") # NON-PORTABLE, UNIX
#         print("\033cMarcin")
#     elif znak == "n":
#         # os.system("clear") # NON-PORTABLE, UNIX
#         print("\033cProgramowanie, Kognitywistyka")
#     elif znak == "c":
#         # os.system("clear") # NON-PORTABLE, UNIX
#         print("\033ccoś innego")
#     else:
#         # os.system("clear") # NON-PORTABLE, UNIX
#         print("\033cNieznany znak")
#     print("------------------------------------")
#     # os.system("clear") # NON-PORTABLE, WINDOWS
#     # os.system("clear") # NON-PORTABLE, UNIX
#     # print("\033c", end="") # PORTABLE (i think?), BUT MESSY (and not allowed)

while True:
    print("Aby zakończyć program, wpisz \"q\".")
    print("Aby wyświetlić imię autora, wpisz \"i\".")
    print("Aby wyświetlić nazwę przedmiotu i kierunek, wpisz \"n\".")
    print("Aby wyświetlić coś innego, wpisz \"c\".")
    znak = input()
    if znak == "q":
        break
    elif znak == "i":
        print("Marcin")
    elif znak == "n":
        print("Programowanie, Kognitywistyka")
    elif znak == "c":
        print("coś innego")
    else:
        print("Nieznany znak")
    input()
    os.system("clear")
