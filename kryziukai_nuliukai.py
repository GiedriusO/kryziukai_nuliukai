lentele = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
zaidejas = "X"
zaidejas_X = 0
zaidejas_O = 0
zaista_kartu = 0



def print_lentele(lentele):
    print("¯¯¯¯¯")
    print(f"{lentele[6]}|{lentele[7]}|{lentele[8]}      Dabar zaidejo {zaidejas} ejimas")
    print(f"{lentele[3]}|{lentele[4]}|{lentele[5]}")
    print(f"{lentele[0]}|{lentele[1]}|{lentele[2]}      Pasirinkite zenklo pozicija skaiciais nuo 1 iki 9")
    print("_____")


def zaidejo_input(lentele):
    try:
        inputas = int(input())
        if inputas >= 1 and inputas <= 9 and lentele[inputas - 1].isdigit():
            lentele[inputas - 1] = zaidejas
            return True
        if inputas <1 or inputas > 9:
            print("Netinkamai ivestas skaicius")
            return False
        else:
            print("Nesukciaujam si vieta jau uzimta :)")
            return False
    except ValueError:
        print("Ups panasu jog ivedete kazka bet tai buvo ne skaicius :)")
        return False


def tikrinti_vertikalei(lentele):
    if (lentele[0] == lentele[3] == lentele[6] or
            lentele[1] == lentele[4] == lentele[7] or
            lentele[2] == lentele[5] == lentele[8]):
        return True
    return False


def tikrinti_horizontaliai(lentele):
    if (lentele[0] == lentele[1] == lentele[2] or
            lentele[3] == lentele[4] == lentele[5] or
            lentele[6] == lentele[7] == lentele[8]):
        return True
    return False


def tikrinti_istrizai(lentele):
    if lentele[6] == lentele[4] == lentele[2] or lentele[0] == lentele[4] == lentele[8]:
        return True
    return False


def tikrinti_lygiasias(lentele):
    for index in lentele:
        if index.isdigit():
            return False
    return True


def ar_zaisti_darkart():
    while True:
        zaisti_vel = str.casefold(input("Ar norite zaisti dar karta? (Y/N) "))
        if zaisti_vel == "y":
            return True
        if zaisti_vel == "n":
            return False


def isvalyti_lentele():
    global lentele, zaidejas
    lentele = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    zaidejas = "O"


def laimejimu_skaitiklis():
    global zaidejas_X, zaidejas_O, zaista_kartu
    zaista_kartu += 1
    print("Rezultatas:")
    print(f"Zaidejas X = {zaidejas_X}")
    print(f"Zaidejas O = {zaidejas_O}")
    print(f"Bendras zaidimu skaicius = {zaista_kartu}")

while True:
    print_lentele(lentele)
    if zaidejo_input(lentele):
        if tikrinti_vertikalei(lentele) or tikrinti_horizontaliai(lentele) or tikrinti_istrizai(lentele):
            print_lentele(lentele)
            print(f"zaidejas {zaidejas} laimejo!! 👍👍  ")
            if zaidejas == "X":
                zaidejas_X += 1
            if zaidejas == "O":
                zaidejas_O += 1
            if ar_zaisti_darkart():
                isvalyti_lentele()
                laimejimu_skaitiklis()
            else:
                break
        if tikrinti_lygiasias(lentele):
            print("Lygiosios ¯\\_(°‿°)_/¯")
            if ar_zaisti_darkart():
                isvalyti_lentele()
            else:
                break
        if zaidejas == "X":
            zaidejas = "O"
        elif zaidejas == "O":
            zaidejas = "X"
