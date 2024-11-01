print("Hallo, gib bitte deinen Namen ein.")
spieler_name = input()

print("Let's go, " ,spieler_name, ". Gib eine Zahl zwischen 1 und 10 ein. Du hast nur 3 Versuche.")

neuer_versuch = "ja"

while neuer_versuch == "ja":
    import random
    n = random.randint(1,10)
    
    for total_guesses in range(3):
        guess = int(input("Gib deine Schätzung ein. "))    
        if guess < n:
            print("Die Zahl ist höher.")
        elif guess > n:
                print("Die Zahl ist niedriger.")
        else:
             break
        
    if guess == n:
        total_guesses = total_guesses + 1
        print("Glückwunsch, du hast die Zahl erraten!")

    if guess != n:
        print("Die richtige Zahl wäre",n,"gewesen.")
    
    print("Wenn du eine neue Runde mit einer neuen Zahl starten willst, tippe ja ein. Mit nein beendest du das Ratespiel.")
    neuer_versuch = input()
print("Ratespiel beendet")