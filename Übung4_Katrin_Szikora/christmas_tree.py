print("Wie hoch soll der Baum sein?")
height = int(input())

# checking min height
while height < 3:
    print("Die Mindesthöhe sollte 3 sein. Bitte geben Sie eine gültige Höhe ein:")
    height = int(input())

# draw top of christmas tree
firstLine = ""
for i in range(height-2):
    firstLine = firstLine + " "
firstLine = firstLine + "*"
print(firstLine)

# draw body of christmas tree
heightBody = height-2       # Spitze und Boden jeweils eine Zeile daher -2
for lineCount in range(1, heightBody+1):
    line = ""
    for spaceSymbol in range(heightBody-lineCount):
        line = line + " "
    for forwardSlashSymbol in range(lineCount):
        line = line + "/"
    line = line + "|"
    for backSlashSymbol in range(lineCount):
        line = line + "\\"
    print(line)

# draw bottom of christmas tree
lastLine = ""
for i in range(height-2):
    lastLine = lastLine + " "
lastLine = lastLine + "|"
print(lastLine)

