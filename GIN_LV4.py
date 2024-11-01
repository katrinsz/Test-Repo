import random
zufallszahl = random.randint(0,100)

zahl_erraten = False    # False & True ersichtlicher als mit break

while not zahl_erraten: # False in Verbindung mit while not = True, geht in Schleife rein
    print("Geben Sie eine Zahl zwischen 0 und 100 ein.")
    geratene_zahl = int(input())

    if geratene_zahl == zufallszahl:
        print("Die Zahl ist richtig")
        zahl_erraten = True

    if geratene_zahl != zufallszahl:
        print("Die Zahl ist falsch.")
