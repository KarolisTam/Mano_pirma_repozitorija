# Pirma užduotis
# Sukurkite klasę "Gyvunas" ir klases "Kate" ir "Suo", kurios paveldi tėvų klasės metodus.
# Kiekviena paveldinti klasė turi turėti savo unikalų "balsas" ir "judeti" metodą.
# Sukurkite kelis skirtingoms klasėms priklausančius objektus, priskirkite jiems vardus ir iškvieskite jų metodus.
# Antra užduotis
# Patikrinkite pirmoje užduotyje sukurtų objektų priklausomybę esančioms klasėms.


class Gyvunai:
    def __init__(self, vardas):
        self.vardas = vardas
   
    def balsas(self):
        pass

    def judeti(self):
        print('Ramiai guli...')

class Kate(Gyvunai):
    def balsas(self):
        print("Mur Mur")

    def judeti(self):
        print('Letai einu')

class Suo(Gyvunai):
    def balsas(self):
        print('Au Au Aaaaaaauuuuuuuuuuuuuuuuu')

    def judeti(self):
        print('Begu greit')

meskenas = Gyvunai('Vagiukas')
kate = Kate('Micius')
suo = Suo('Dante')

print(meskenas.vardas)
meskenas.balsas()
meskenas.judeti()

print(suo.vardas)
suo.balsas()
suo.judeti()

print(kate.vardas)
kate.balsas()
kate.judeti()