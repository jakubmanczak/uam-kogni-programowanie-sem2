class Sim:
    def __init__(self, wiek, nastroj, plec, zawod, poziom_najedzenia):
        self.lista_nastrojow = ["zadowolony", "smutny", "radosny", "zmartwiony", "neutralny"]
        self.lista_plci = ["kobieta", "mezczyzna", "nonbinary", "inna"]
        self.nr_nastroju = nastroj
        self.nr_plci = plec
        self.zawod = zawod
        self.poziom_najedzenia = poziom_najedzenia
        self.wiek = wiek
        print("Sim utworzony.")
        # print(f"Nastrój sima to: {self.lista_nastrojow[self.nr_nastroju]}")
    def wyswietl_liste_nastrojow(self):
        for nastroj in self.lista_nastrojow:
            print(nastroj)
    def ustaw_nastroj(self, nr_nastroju):
        self.nr_nastroju = nr_nastroju
    def wyswietl_aktualny_nastroj(self):
        print(f"Nastrój: {self.lista_nastrojow[self.nr_nastroju]}")
    def ustaw_plec(self, nr_plci):
        self.plec = nr_plci
    def wyswietl_plec(self):
        print(f"Płeć sima to: {self.lista_plci[self.plec]}")
    def ustaw_zawod(self, nowy_zawod):
        self.zawod = nowy_zawod
    def wyswietl_zawod(self):
        print(f"Zawód sima to: {self.zawod}")
    def ustaw_poziom_najedzenia(self, nowy_poziom_najedzenia):
        self.poziom_najedzenia = nowy_poziom_najedzenia
    def wyswietl_poziom_najedzenia(self):
        print(f"Poziom najedzenia tego sima: {self.poziom_najedzenia}/100")
    def powitanie(self):
        print("Cześć, to ja, Sim. Sim z Sim City!")
    def wyswietl_wiek(self):
        print(f"Wiek sima to: {self.wiek}")

Marek = Sim(20, 0, 1, "student", 100)
