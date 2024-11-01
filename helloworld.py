noten = []

print("Wieviele Noten möchtest du eingeben?")
anzahlNoten = int(input())

if(anzahlNoten > 0 and anzahlNoten < 5):
    for i in range(anzahlNoten):
        noten.append(int(input()))


    sum = 0
    for i in range(anzahlNoten):
        print("i ist: " + str(i))
        print("Note auf dem Index " + str(i)+ " ist " + str(noten[i]))
        sum = sum + noten[i]
        print("aktuelle Summe: " + str(sum))

    ergebnis = sum / anzahlNoten
    print(ergebnis)
