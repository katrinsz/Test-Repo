Frage1 = "Wie viele Kontinente hat die Erde?"
Auswahl1 = "5,6,7,8"

Frage2 = "Welcher ist der höchste Berg der Welt?"
Auswahl2 = "Mount Everest, Großglockner, Broad Peak, Mount Godwin Austen"

Frage3 = "In welchem Land erstreckt sich die Sahara nicht?"
Auswahl3 = "Ägypten, Marokko, Südafrika, Tunesien"

Frage4 = "Wie oft kommen Schaltjahre vor?"
Auswahl4 = " alle 2 Jahre, alle 3 Jahre, alle 4 Jahre, alle 5 Jahre"

Frage5 = "Wie hieß der erste Präsident der Vereinigten Staaten?"
Auswahl5 = "George Washingtion, John Adams, Thomas Jefferson, JFK"

print(Frage1, Auswahl1)
antwort1 = int (input())
if (antwort1 == 7):
    print("Die Antwort ist korrekt")
if (antwort1 != 7):
    print("Die Antwort ist falsch")

print(Frage2, Auswahl2)
antwort2 = input()
if(antwort2 == "Mount Everest"):
    print("Die Antwort ist korrekt")
if(antwort2 != "Mount Everest"):
    print("Die Antwort ist falsch")

print(Frage3, Auswahl3)
antwort3 = input()
if(antwort3 == "Südafrika"):
    print("Die Antwort ist korrekt")
if(antwort3 != "Südafrika"):
    print("Die Antwort ist falsch")

print(Frage4, Auswahl4)
antwort4 = input()
if(antwort4 == "alle 4 Jahre"):
    print("Die Antwort ist korrekt")
if(antwort4 != "alle 4 Jahre"):
    print("Die Antwort ist falsch")

print(Frage5, Auswahl5)
antwort5 = input()
if(antwort5 == "George Washington"):
    print("Die Antwort ist korrekt")
if(antwort5 != "George Washington"):
    print("Die Antwort ist falsch")