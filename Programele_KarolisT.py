print("---------------------------")
print('Sveiki atvykę į žaidima Q&A')
print("---------------------------")
print("----------Sekmės-----------")

taskai = 0

klausimas1 = (input("Kaip vadinasi Lietuvos sostine?:"))
if klausimas1 == "Vilnius" or klausimas1 == "vilnius":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas.\nTeisingas atsakymas buvo: Vilnius")

print("-----------------------------")
klausimas2 = (input("Kurias metais buvo sukurta programavimo kalba Python?:"))
if klausimas2 == "1991":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas..\nTeisingas atsakymas buvo: 1991")

print("-----------------------------")

klausimas3 = (input("Kelintais metais Code Academy pradėjo savo veikla?:"))
if klausimas3 == "2016":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas.\nTeisingas atsakymas buvo: 2016") 
print("-----------------------------")

klausimas4 = (input("Kelinta valanda pietų pertrauka?:"))
if klausimas4 == "12":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas.\nTeisingas atsakymas buvo: 12")
print("-----------------------------")

klausimas5 = (input("Kur galima pritaikyti Python?:  "))
if klausimas5 == "Visur" or klausimas5 == "visur":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas.\nTeisingas atsakymas buvo: visur")
print("-----------------------------")

klausimas6 = (input("Ar Kaunas buvo laikinoji sostinė?: "))
if klausimas6 == "Taip" or klausimas6 == "taip":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas..\nTeisingas atsakymas buvo: Taip")
print("-----------------------------")

klausimas6 = (input("Ar driežai gali užsiauginti nauja uodega: "))
if klausimas6 == "Taip" or klausimas6 == "taip":
    print("Jūsų atsakymas teisingas")
    taskai += 1
else:
    print("Jūsų atsakymas klaidingas..\nTeisingas atsakymas buvo: Taip")

print("-------------------------------")
print("")
print("Viso teisgai atsakėte: " + str(taskai))
print('Geros dienos') 





