# class Sim:
#     def __init__(self, nastroj):
#         self.lista_nastrojow = ["zadowolony", "smutny", "radosny", "zmartwiony", "neutralny"]
#         self.nr_nastroju = nastroj
#         print("Sim utworzony.")
#         print(f"Nastrój sima to: {self.lista_nastrojow[self.nr_nastroju]}")
#     def wyswietl_liste_nastrojow(self):
#         for nastroj in self.lista_nastrojow:
#             print(nastroj)
#     def ustaw_nastroj(self, nastroj):
#         self.nr_nastroju = nastroj
#     def wyswietl_aktualny_nastroj(self):
#         print(f"Nastrój: {self.lista_nastrojow[self.nr_nastroju]}")
#     def powitanie(self):
#         print("Cześć, to ja, Sim. Sim z Sim City!")
#         self.wiek = 20
#     def wyswietl_wiek(self):
#         print(f"Wiek sima to: {self.wiek}")

# Marek = Sim(3)
# Alina = Sim(0)
# Marek.ustaw_nastroj(1)
# Marek.wyswietl_aktualny_nastroj()

# print("Na jaki nastrój zmienić nastrój Marka?", end="")
# nr_nowego_nastroju = int(input())
# Marek.ustaw_nastroj(nr_nowego_nastroju)
# Marek.wyswietl_aktualny_nastroj()

class Student:
    def __init__(self):
        print("Pojawił się nowy student! Jak ma na imię?")
        self.imie = input()
        print(f"Ile lat ma {self.imie}?")
        self.wiek = int(input())
    def wyswietl_podsumowanie(self):
        print(f"Ten student ma na imie {self.imie} i ma {self.wiek} lat.")

st1 = Student()
st2 = Student()
st1.wyswietl_podsumowanie()
st2.wyswietl_podsumowanie()
