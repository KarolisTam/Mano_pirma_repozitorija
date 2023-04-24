# Sukurkite knygų klasę, kuri turėtų privačius kintamuosius: pavadinimas, autorius, buklė ir puslapių skaičius, ir metodus jiems gauti.
# Sukurkite metodą, kuris leistų pakeisti knygos būklę, kur galimos reikšmės yra tik 'patenkinama', 'prasta', 'atnaujinta', 'sugadinta'.
# Sukurkite metodą, kuris leistų sumažinti knygos puslapių skaičių, naudodamas sukurtą vidinį privatų metodą, perrašantį tą reikšmę. Turi neigi padidinti puslapių skaičiaus.

class Knyga():
    def __init__(self, pavadinimas, autorius, bukle, puslapiai):
        self.__pavadinimas = pavadinimas
        self.__autorius = autorius
        self.__bukle = bukle
        self.__puslapiai = puslapiai

    def gauti_pavadinima(self): #Funkicja kuri istrauke reiksmia is klases
        return self.__pavadinimas #return naudoja, kad isgauti pavadinima, be return, negaunam atsakymo
    
    def gauti_autorius(self):
        return self.__autorius
    
    def gauti_bukle(self):
        return self.__bukle
    
    def gauti_puslapius(self):
        return self.__puslapiai

    def keisti_bukle(self, bukle,):
        if bukle in ('patenkinama', 'prasta', 'atnaujinta', 'sugadinta'):
            self.__bukle = bukle
        else:
            print(f'negalima pakeisti būklės į {bukle}.')

    def __nauji_puslapiai(self, puslapiai):
        self.__puslapiai = puslapiai

    def panaikinti_puslapiai(self, puslapiai):
        if abs(puslapiai) <= self.__puslapiai:
            self.__nauji_puslapiai(self.__puslapiai - abs(puslapiai))
        else:
            self.__puslapiai = 0


knyga = Knyga("Alchemikas", "Paulo Coelho", "nauja", 168)

knyga.panaikinti_puslapiai(200)
knyga.keisti_bukle('sugadinta')
print(knyga.gauti_pavadinima())
print(knyga.gauti_autorius())
print(knyga.gauti_bukle())
print(knyga.gauti_puslapius())