class Sim:
    def __init__(self, imie):
        self.__imie = imie
        self.__relacje = {}
    def podaj_imie(self):
        return self.__imie
    def zmien_relacje(self, drugi_sim, punkty):
        imie_drugiego_sima = drugi_sim.podaj_imie()
        if imie_drugiego_sima not in self.__relacje:
            self.__relacje[imie_drugiego_sima] = punkty
        else:
            self.__relacje[imie_drugiego_sima] += punkty
    def pokaż_relację_z(self, drugi_sim):
        print(f"{self.podaj_imie()} ma {self.zwróć_relację_z(drugi_sim)} punktów relacji z {drugi_sim.podaj_imie()}")
    def zwróć_relację_z(self, drugi_sim):
        return self.__relacje[drugi_sim.podaj_imie()]
    def _interakcja(self, drugi_sim, wartosc):
        imie_drugiego_sima = drugi_sim.podaj_imie()
        self.zmien_relacje(drugi_sim, wartosc)
        drugi_sim.zmien_relacje(self, wartosc)
    def daj_prezent(self, drugi_sim):
        self._interakcja(drugi_sim, 20)
    def rozmawiaj_z(self, drugi_sim):
        self._interakcja(drugi_sim, 10)
    def pokłóć_się_z(self, drugi_sim):
        self._interakcja(drugi_sim, -10)
    def pobij_się_z(self, drugi_sim):
        self._interakcja(drugi_sim, -20)

sim1 = Sim("jakdak")
sim2 = Sim("jukiewicz")

sim1.zmien_relacje(sim2, 0)
sim1.pokaż_relację_z(sim2)
sim1.daj_prezent(sim2)
sim1.pokaż_relację_z(sim2)
sim1.rozmawiaj_z(sim2)
sim1.pokaż_relację_z(sim2)
sim1.pokłóć_się_z(sim2)
sim1.pokaż_relację_z(sim2)
sim1.pobij_się_z(sim2)
sim1.pokaż_relację_z(sim2)
sim1.daj_prezent(sim2)
sim1.pokaż_relację_z(sim2)
sim1.rozmawiaj_z(sim2)
sim1.pokaż_relację_z(sim2)
