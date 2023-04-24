zurnalas = []
print('-----Sveiki atvykę į išlaidus suvestinę-----')
atlyginimas = float(input("Įvesti šio men. atlyginimą: "))
print('--------------------------------------------')
atlyginimo_mokestis_proc = float(input("Įvesti mokeščio procentų dydį: "))
print('--------------------------------------------')
balansas = atlyginimas * (1 - atlyginimo_mokestis_proc / 100)
zurnalas.append(balansas)


while True:
    print('Porgramų pasirinkimas: Kuras(1), Blanasas(2), Buto nuoma(3), Dienos išlaidos(4), Pramogos(5), Zurnalas(6), Iseiti(9)')
    pasirinkimas = int(input("Įveskite pageidautina programą: "))
    print('-----------------------------------------------')
    if pasirinkimas == 1:
        kuras = int(input("Įveskite suma kuria išleidžiate kurui: "))
        zurnalas.append(-kuras)
        print(f"Jūsų kuro išlaidos: {kuras}")
        print('--------------------------------------------')

    elif pasirinkimas == 2:
        print(f'Jūsu dabartinis balansas: {balansas} Eurų.')
        print('--------------------------------------------')

    elif pasirinkimas == 3:
        butas = int(input('Įveskite buto nuomos išlaidas: '))
        print('--------------------------------------------')
        zurnalas.append(-butas)

    elif pasirinkimas == 4:
        dienos_islaidos = int(input('Įveskite dienos išlaidas: '))
        print('--------------------------------------------')
        zurnalas.append(-dienos_islaidos)

    elif pasirinkimas == 5:
        pramogos = int(input('Įveskite progomų išlaidas: '))
        print('--------------------------------------------')
        zurnalas.append(-pramogos)
    elif pasirinkimas == 6:
        bendras = 0
        for irasas in zurnalas:
            print(irasas)
            bendras += irasas
        print(f'balansas: {bendras}')
        print('--------------------------------------------')
    elif pasirinkimas == 9:
        print('-------Geros dienos--------')
        break