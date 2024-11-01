import random

def wurfeln(anzahl_wurfel, augenzahl):
    return sum(random.randint(1, augenzahl) for anzahl_durchlaeufe in range(anzahl_wurfel))

def user_input():
    try:
        anzahl_wurfel = int(input("Wieviele Würfel? "))
        augenzahl = int(input("Augenzahl Würfel: "))
        return anzahl_wurfel, augenzahl
    except ValueError:
        print("Bitte geben Sie gültige Zahlen ein.")
        return user_input()

def play_dice_game():
    weiter = True
    while weiter:
        anzahl_wurfel, augenzahl = user_input()
        summe_augenzahl = wurfeln(anzahl_wurfel, augenzahl)
        
        print("Gesamtsumme:", summe_augenzahl)

        print("Weiter? (ja/nein)")
        weiter = input()
        if(weiter == "ja"):
          weiter = True
        else:
          weiter = False

play_dice_game()









