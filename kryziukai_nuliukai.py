# Sukurti kryžiukų/nuliukų žaidimą, kuris:
# Leistų žaisti dviems žaidėjams (X ir O)
# Teisingai fiksuotų vieno iš žaidėjų laimėjimą arba lygiasias ir stabdytų žaidimą
# Žaidimas vyktų konsolėje, grafinio interfeiso nereikia (bet galima daryti, tada konsolės nebereikia)
# Sukurtą žaidimą paskelbti github repozitorijoje, nuorodą paskelbti teamsuose, tam skirtoje užduotyje (Assignments)
# 1 lentele
# 2 zaidejas
# 3 inputas
# 4 kazkokio loop jog zaisti
# 5 tikrinti ar laimejo/lygiosios ir uzbaigti loop

lentele = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
zaidejas = "x"
zaidimas_vyksta = True

def print_lentele():
    print(lentele[0] + "|" + lentele[1] + "|" + lentele[2])
    print(lentele[3] + "|" + lentele[4] + "|" + lentele[5])
    print(lentele[6] + "|" + lentele[7] + "|" + lentele[8])

def zaidejo_input():
    inputas = int(input("iveskite skaiciu nuo 1 iki 9"))
    if inputas <= 1 or inputas <= 9:
        lentele[inputas-1] = zaidejas

def tikrinti_vertikalei():
    if (lentele[0]==lentele[3]==lentele[6] or
            lentele[1]==lentele[4]==lentele[7] or
            lentele[2]==lentele[5]==lentele[8]):
        print("sveikiname jus laimejote")

def tikrinti_horizontaliai():
    if (lentele[0]==lentele[1]==lentele[2] or
            lentele[3]==lentele[4]==lentele[5] or
            lentele[6]==lentele[7]==lentele[8]):
        print("sveikiname jus laimejote")

def tikrinti_istrizai():
    if lentele[6]==lentele[4]==lentele[2] or lentele[0]==lentele[4]==lentele[8]:
        print("veikiname jus laimejote")

def tikrinti_lygiasias():

while zaidimas_vyksta:
    if zaidejas == "x":
        zaidejas = "o"
    elif zaidejas == "o":
        zaidejas = "x"
    print(print_lentele())
    zaidejo_input()
    tikrinti_vertikalei()
    tikrinti_horizontaliai()
    tikrinti_istrizai()