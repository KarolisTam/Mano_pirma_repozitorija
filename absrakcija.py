class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka'):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva
        self.max_greitis = 200
        self.__greitis = 0

    # šį privatų abstraktų metodą panaudosime keliose vietose
    def __keisti_greiti(self, greitis):
        if greitis > self.max_greitis:
            greitis = self.max_greitis
        if greitis < -10:
            greitis = -10
        self.__greitis = greitis
        return greitis

    # šį viešą abstraktų metodą irgi panaudosime keliose vietose
    def vaziuoti(self):
        greitis = self.__greitis
        if greitis > 0:
            print(f"važiuoju {self.__greitis} km/h greičiu")
        elif greitis < 0:
            print(f"važiuoju {abs(self.__greitis)} km/h greičiu atgal")
        else:
            print("stoviu")

    def didinti_greiti(self, pagreitis=10):
        # panaudojame privatų metodą maksimalaus greičio ribojimui
        self.__keisti_greiti(self.__greitis + pagreitis)
        # panaudojame vieša metodą važiavimo situacijai išvesti
        self.vaziuoti()

    def mazinti_greiti(self, pagreitis=10):
        # panaudojame privatų metodą maksimalaus greičio ribojimui
        self.__keisti_greiti(self.__greitis - pagreitis)
        # panaudojame vieša metodą važiavimo situacijai išvesti
        self.vaziuoti()
    

guolis = Automobilis("Volkswagen", "Golf")
print(guolis.marke, guolis.modelis, guolis.metai, guolis.spalva)
guolis.vaziuoti()
guolis.didinti_greiti()
guolis.didinti_greiti()
guolis.didinti_greiti(20)
guolis.didinti_greiti(170)
guolis.mazinti_greiti(100)
guolis.mazinti_greiti(50)
guolis.mazinti_greiti(50)
guolis.mazinti_greiti()
guolis.didinti_greiti()

class Elektromobilis(Automobilis):
    pass


tesla = Elektromobilis("Tesla", "Model-3")
print(tesla.marke, tesla.modelis, tesla.metai, tesla.spalva) # Tesla Model 3 2023 pilka
tesla.vaziuoti() # stoviu
tesla.didinti_greiti(100) # važiuoju 100 km/h greičiu

class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka', **kwargs):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva
        self.max_greitis = 200
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.__greitis = 0

guolis = Automobilis("Volkswagen", "Golf", kuro_tipas="benzinas", variklis="1.6ti")
print(f"{guolis.marke} {guolis.modelis}, {guolis.metai} m. {guolis.spalva}. Variklis: {guolis.variklis} {guolis.kuro_tipas}. Max. {guolis.max_greitis} km/h")
# Volkswagen Golf, 2023 m. pilka. Variklis: 1.6ti benzinas. Max. 200 km/h
astra = Automobilis("Opel", "Astra", kuro_tipas="benzinas", variklis="1.6", max_greitis=160)
print(f"{astra.marke} {astra.modelis}, {astra.metai} m. {astra.spalva}. Variklis: {astra.variklis} {astra.kuro_tipas}. Max. {astra.max_greitis} km/h")
# Opel Astra, 2023 m. pilka. Variklis: 1.6 benzinas. Max. 160 km/h

def informacija(obj):
    print(f"{obj.marke} {obj.modelis}, {obj.metai} m. {obj.spalva}. Variklis: {obj.variklis} {astra.kuro_tipas}. Max. {obj.max_greitis} km/h")    

informacija(guolis)
informacija(astra)