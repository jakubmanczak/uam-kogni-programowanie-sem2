import random

class Walczący():
    def __init__(self, imie):
        self.__imie = imie
        self.__hp = random.randint(25, 100)
        self.__pkt_ataku = random.randint(10, 20)
    def pobierz_hp(self):
        return self.__hp
    def pobierz_imie(self):
        return self.__imie
    def pobierz_pkt_ataku(self):
        return self.__pkt_ataku
    def obrona(self, obrazenia):
        self.__hp -= obrazenia
        if self.__hp < 0:
            self.__hp = 0
    def status(self):
        if self.__hp == 0:
            print(f"{self.__imie} nie żyje!")
        else:
            print(f"{self.__imie} ma {self.__hp} punktów życia!")
    def zyje(self):
        if self.__hp != 0:
            return True
        return False
    def atakuj(self, przeciwnik):
        pass

class Czarodziej(Walczący):
    def __init__(self, imie):
        super().__init__(imie) # tego nie wolno na projektach...
        self.__poprzedni_atak = ""
        self.__pkt_many = random.randint(21, 30)
    def atakuj(self, przeciwnik):
        if self.__poprzedni_atak == "melee": # więc mana
            przeciwnik.obrona(self.pobierz_pkt_ataku())
            self.__poprzedni_atak = "mana"
            print(f"Czarodziej {self.pobierz_imie()} zaatakował {przeciwnik.pobierz_imie()}! Zadał {self.pobierz_pkt_ataku()} obrażeń ciosem fizycznym.")
        else: # więc melee
            przeciwnik.obrona(self.__pkt_many)
            self.__poprzedni_atak = "melee"
            print(f"Czarodziej {self.pobierz_imie()} zaatakował {przeciwnik.pobierz_imie()}! Zadał {self.__pkt_many} obrażeń ciosem magicznym.")


class Wojownik(Walczący):
    def __init__(self, imie):
        super().__init__(imie) # tego nie wolno na projektach...
    def atakuj(self, przeciwnik):
        przeciwnik.obrona(self.pobierz_pkt_ataku())
        print(f"Wojownik {self.pobierz_imie()} zaatakował {przeciwnik.pobierz_imie()}! Zadał {self.pobierz_pkt_ataku()} obrażeń.")

gracz1 = Czarodziej("jakdak")
gracz2 = Wojownik("jukiewicz")

while gracz1.zyje() and gracz2.zyje():
    gracz1.atakuj(gracz2)
    gracz2.status()
    if gracz2.zyje():
        gracz2.atakuj(gracz1)
        gracz1.status()
    if not(gracz1.zyje()):
        print(f"{gracz2.pobierz_imie()} wygrał!")
    if not(gracz2.zyje()):
        print(f"{gracz1.pobierz_imie()} wygrał!")
