width = int(input("Gib die gewünschte Breite der Raute ein: "))

if width % 2 == 0: # % = modulo operator, berechnet Rest einer Division
    width += 1  # Breite muss ungerade sein, damit die Raute symmetrisch ist

# obere Hälfte der Raute
for i in range(1, width + 1, 2):  # Parameter range-Funktion = start, stop, step
    spaces = " " * int((width - i) / 2)
    stars = "*" * i
    print(spaces + stars)

# untere Hälfte der Raute
for i in range(width - 2, 0, -2):
    spaces = " " * int((width - i) / 2)
    stars = "*" * i
    print(spaces + stars)





