# schreiben/hinzufügen
file = open("demofile.txt", "a")
file.write("neuer Text im File")
file.write("\n")
file.write("Neue Zeile")
file.close()
file = open("demofile.txt")
inhaltfile = file.read()
print(inhaltfile)