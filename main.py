import random






def paraSkaitli(skaits):
    print("Varbutiba para skaitli ir:" + str(1 * skaits) + "/" + str(2 * skaits))


def neparskaitli(skaits):
    if a == 1:
        print("Iespēja ir 100 %")
    elif a == 2:
        print("Iespēja ir 83 %")
    elif a == 3:
        print("Iespēja ir 66 %")
    elif a == 4:
        print("Iespēja ir 50 %")
    elif a == 5:
        print("Iespēja ir 33 %")

def vienadiskaitli(skaits):
    print("Varbutiba vienad skaitli ir: " + str(1 * skaits) + "/" + str(6 * skaits))


def divivienadi(skaits):
    kaulins = 1 * 2
    print("Varbutiba divi vienadi skaitli ir: " + str(kaulins) + "/" + str(6 * skaits))




    if __name__ == '__main__':
        print("SUIIIIIIII...")
        print("What do you want? \n1-is a varbutiba para skaitli\n2-varbutiba neparaskaitli\n3-varbutiba vienadiskaitli\n4-varbutiba divivienadi\n5-playRound")
        metode = int(input("type 1-5:"))
        skaits = int(input("how much dice"))
        if metode == 1:
            paraSkaitli(skaits)
        elif metode == 2:
            neparskaitli(skaits)
        elif metode == 3:
            vienadiskaitli(skaits)
        elif metode == 4:
            divivienadi(skaits)
        elif metode == 5:
