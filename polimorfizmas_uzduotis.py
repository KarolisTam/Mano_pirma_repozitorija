# sukurkite darbuotojų klasę su savybėmis vardas, pavarde ir atlyginimas, kuri turėtų metodą atspausdinantį darbuotojo informaciją.
# Sukurkite administratoriaus klasę, kuri paveldėtų savybes iš darbuotojo klasės.
# Sukurkite vadovo klasę, kuri paveldėtų savybes iš darbuotojo klasės ir turėtų papildomą savybę "premija" bei metodą, kuris atspausdins darbuotojo informaciją.
# Sukurkite kelis kiekvienos klasės objektus ir iškvieskite informacijos spausdinimo metodą.


class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas=1000):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def info(self):
        print(f'{self.vardas} {self.pavarde}, atlyginimas: {self.atlyginimas} €')


class Administratorius(Darbuotojas):
    def __init__(self, vardas, pavarde, atlyginimas):
        super().__init__(vardas, pavarde, atlyginimas)


class Vadovas(Darbuotojas):
    def __init__(self, vardas, pavarde, atlyginimas, premija):
        super().__init__(vardas, pavarde, atlyginimas)
        self.premija = premija

    def info(self):
        super().info()
        print(f'Premija: {self.premija} €')


darbuotojas1 = Darbuotojas('Kazys', 'Juozas')
darbuotojas2 = Darbuotojas('Petras', 'Petraitis', 1200)
darbuotojas3 = Administratorius('Juozas', 'Juozaitis', 900)
vadovas1 = Vadovas('Antanas', 'Antanaitis', 1500, 500)

darbuotojai = [darbuotojas1, darbuotojas2, darbuotojas3, vadovas1]

for darbuotojas in darbuotojai:
    darbuotojas.info()