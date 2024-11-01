weiter = "ja"

while weiter == "ja":
    Einheit = input("In welcher Einheit ist die Ausgangszahl? ")
    Wert = int(input("Gib den Wert der Geschwindigkeit ein. "))
    Umrechnungseinheit = input("In welche Einheit soll umgerechnet werden? ")
    
    kmh_to_mph = Wert / 1.609
    mph_to_kmh = Wert * 1.609
    kmh_to_kn = Wert / 1.852
    kn_to_kmh = Wert * 1.852
    mph_to_kn = Wert / 1.151
    kn_to_mph = Wert * 1.151

    if (Einheit == "kmh" and Umrechnungseinheit == "mph"):
        print("Ergibt umgerechnet", kmh_to_mph, "mph")

    if (Einheit == "mph" and Umrechnungseinheit == "kmh"):
        print("Ergibt umgerechnet", mph_to_kmh, "kmh")

    if (Einheit == "kmh" and Umrechnungseinheit == "kn"):
        print("Ergibt umgerechnet", kmh_to_kn, "kn")

    if (Einheit == "kn" and Umrechnungseinheit == "kmh"):
        print("Ergibt umgerechnet", kn_to_kmh, "kmh")

    if (Einheit == "mph" and Umrechnungseinheit == "kn"):
        print("Ergibt umgerechnet", mph_to_kn, "kn")

    if (Einheit == "kn" and Umrechnungseinheit == "mph"):
        print("Ergibt umgerechnet", kn_to_mph, "mph")

    print("Möchtest du weitere Werte konvertieren?")
    weiter = input()
print("Konverter beendet")