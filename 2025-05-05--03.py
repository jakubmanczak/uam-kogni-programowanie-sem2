class Telewizor:
    def __init__(self):
        self.lista_kanalow = ["TVP1", "TVP2", "TVPinfo", "TVN", "Cartoon Network", "Disney XD"]
        self.nr_kanalu = 0
        self.glosnosc = 15
        print(f"Oto telewizor! Dzięki opatrzności rządu zawsze z początku ustawiony na {self.lista_kanalow[self.nr_kanalu]}. Głośność {self.glosnosc}.")
    def ustaw_glosnosc(self, nowa_glosnosc):
        if nowa_glosnosc >= 0 and nowa_glosnosc <= 20:
            self.glosnosc = nowa_glosnosc
            print(f"Ustawiono głośność na {nowa_glosnosc}.")
        else:
            print("Nie można zmienić głośności na wartość poniżej 0 lub powyżej 20.")
    def zwieksz_glosnosc(self):
        self.ustaw_glosnosc(self.glosnosc + 1)
    def zmniejsz_glosnosc(self):
        self.ustaw_glosnosc(self.glosnosc - 1)
    def wyswietl_liste_kanalow(self):
        print(f"Telewizor obsługuje następujące kanały: {self.lista_kanalow}")
    def wyswietl_aktualny_kanal(self):
        print(f"Telewizor jest aktualnie ustawiony na kanał {self.nr_kanalu}: {self.lista_kanalow[self.nr_kanalu]}.")
    def zmien_kanal(self, nowy_nr_kanalu):
        self.nr_kanalu = nowy_nr_kanalu
        print(f"Telewizor został przełączony na kanał {self.nr_kanalu}: {self.lista_kanalow[self.nr_kanalu]}.")
    def przeskocz_kanal_wyzej(self):
        self.nr_kanalu += 1
        if self.nr_kanalu == len(self.lista_kanalow):
            self.nr_kanalu = 0
        print(f"Przeskoczono na kanał wyżej: {self.lista_kanalow[self.nr_kanalu]} ({self.nr_kanalu})")
    def przeskocz_kanal_nizej(self):
        self.nr_kanalu -= 1
        if self.nr_kanalu < 0:
            self.nr_kanalu = len(self.lista_kanalow) - 1
        print(f"Przeskoczono na kanał niżej: {self.lista_kanalow[self.nr_kanalu]} ({self.nr_kanalu})")
    def tryb_interaktywny(self):
        print("Witaj w trybie interaktywnym telewizora. Co chcesz zrobić?")
        while True:
            print("Podejmij wybór następnej akcji.")
            print("k+ = skok o kanał w górę")
            print("k- = skok o kanał w dół")
            print("v+ = głośność w dół")
            print("v- = głośność w górę")
            print("q  = wyjście z trybu interaktywnego telewizora")
            print("Co chcesz zrobić? Podaj: ", end="")
            wybor = input()
            if wybor == "k+":
                self.przeskocz_kanal_wyzej()
            elif wybor == "k-":
                self.przeskocz_kanal_nizej()
            elif wybor == "v+":
                self.zwieksz_glosnosc()
            elif wybor == "v-":
                self.zmniejsz_glosnosc()
            elif wybor == "q":
                break
            else:
                print("Nieznany wybór. jeszcze raz.")


tv = Telewizor()
tv.tryb_interaktywny()
tv.wyswietl_liste_kanalow()
tv.wyswietl_aktualny_kanal()
# print("Podaj indeks kanału na który przełączyć telewizor: ", end="")
# tv.zmien_kanal(int(input()))
tv.zmien_kanal(3)
tv.wyswietl_aktualny_kanal()
for i in range(5):
    tv.przeskocz_kanal_wyzej()
for i in range(3):
    tv.przeskocz_kanal_nizej()
for i in range(6):
    tv.zwieksz_glosnosc()
tv.ustaw_glosnosc(3)
for i in range(4):
    tv.zmniejsz_glosnosc()
