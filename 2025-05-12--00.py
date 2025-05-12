import random

# class Wojownik():
#     def __init__ (self, imie):
#         self.__pkt_zycia=random.randint(1 ,100)
#         self.__pkt_ataku=random.randint(1 ,20)
#         self.__pkt_many=random.randint(10, 35)
#         self.__tura = "melee"
#         self.__imie = imie
#     def obrona(self,obrazenia):
#         self.__pkt_zycia-=obrazenia
#         if self.__pkt_zycia<0:
#             self.__pkt_zycia=0
#     def jest_zywy(self):
#         if self.__pkt_zycia == 0:
#             return False
#         return True
#     def pobierz_wartosc_atakowa(self):
#         if self.__tura == "melee":
#             self.__tura = "mana"
#             return self.__pkt_ataku
#         else:
#             self.__tura = "melee"
#             return self.__pkt_many
#     def pobierz_pkt_ataku (self):
#         return self.__pkt_ataku
#     def pobierz_pkt_zycia (self):
#         return self.__pkt_zycia
#     def pobierz_imie(self):
#         return self.__imie

# gracz1 = Wojownik("jakdak")
# gracz2 = Wojownik("jukiewicz")

# while gracz1.pobierz_pkt_zycia() > 0 and gracz2.pobierz_pkt_zycia() > 0:
#     gracz1.obrona(gracz2.pobierz_wartosc_atakowa())
#     print(f"{gracz1.pobierz_imie()} otrzymał {gracz2.pobierz_wartosc_atakowa()} obrażeń! Pozostało mu {gracz1.pobierz_pkt_zycia()} pkt życia.")
#     if not(gracz1.jest_zywy()):
#         print(f"{gracz1.pobierz_imie()} nie żyje! {gracz2.pobierz_imie()} wygrał!")
#         break
#     gracz2.obrona(gracz1.pobierz_wartosc_atakowa())
#     print(f"{gracz2.pobierz_imie()} otrzymał {gracz1.pobierz_wartosc_atakowa()} obrażeń! Pozostało mu {gracz2.pobierz_pkt_zycia()} pkt życia.")
#     if not(gracz2.jest_zywy()):
#         print(f"{gracz2.pobierz_imie()} nie żyje! {gracz1.pobierz_imie()} wygrał!")
#         break




# Wojownik.py, wersja lepsza bo czemu obrona jest główną wywoływaną metodą, a nie atak!!!
class Wojownik():
    def __init__(self, imie):
        self.__imie = imie
        self.__hp = random.randint(25, 100)
        self.__phys_atk = random.randint(5, 20)
        self.__mana_atk = random.randint(1, 40)
        self.__poprzedni_atak = ""
    def pobierz_hp(self):
        return self.__hp
    def pobierz_imie(self):
        return self.__imie
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
    def atakuj(self, drugi_wojownik):
        if self.__poprzedni_atak == "melee": # a więc mana
            drugi_wojownik.obrona(self.__mana_atk)
            self.__poprzedni_atak = "mana"
            print(f"{self.__imie} zaatakował {drugi_wojownik.pobierz_imie()}! Użył magii, zadając {self.__mana_atk} punktów obrażeń!")
        else: # a więc melee
            drugi_wojownik.obrona(self.__phys_atk)
            self.__poprzedni_atak = "melee"
            print(f"{self.__imie} zaatakował {drugi_wojownik.pobierz_imie()}! Użył siły, zadając {self.__phys_atk} punktów obrażeń!")


gracz1 = Wojownik("jakdak")
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
