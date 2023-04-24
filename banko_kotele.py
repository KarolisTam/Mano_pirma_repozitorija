class BankoSaskaita:
    def __init__(self, saksaitos_numeris, savininkas, balansas, pin):
        self.saksaitos_numeris = saksaitos_numeris
        self.savininkas = savininkas
        self.__balanasas = balansas
        self.__pin = pin

    def pinigu_nuemimas(self,suma, pin):
        if pin == self.__pin:
            self.__balanasas -= suma
            print(f'{suma} $ buvo sėkmingai nuskaityta iš jūsų sąsakitos. Dabartinis sąskaitos liktus {self.__balanasas} $')
        else:
            print('Įvedėte klaidingai slaptažodį, bandykite dar kartą.')

    def pinigu_prideti(self,suma, pin):
        if pin == self.__pin:
            self.__balanasas += suma
            print(f'{suma} $ buvo sėkmingai nukeliavo į jūsų sąskaitą. Dabartinis sąsakitos likutis {self.__balanasas} $')
        else:
            print('Įvedėte klaidingai slaptažodį, bandykite dar kartą.')
    
saskaita = BankoSaskaita('LT123456789', 'Jonas Jonaitis', 1000, 1234)
saskaita.pinigu_nuemimas(10, 1122)
saskaita.pinigu_nuemimas(240, 1234)
saskaita.pinigu_nuemimas(120, 12345)
saskaita.pinigu_prideti(5000, 1234)