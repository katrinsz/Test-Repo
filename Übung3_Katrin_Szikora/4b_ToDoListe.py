myTasks = []
tasksDone = []

def menu():
    print("Meine To Do Liste")
    print("1. Aufgabe hinzufügen")
    print("2. Zu erledigende Aufgaben ansehen")
    print("3. Aufgabe erledigen")
    print("4. Erledigte Aufgaben ansehen")
    print("5. Text Aufgabe ändern")

def addTask():
    task = input("Gib eine neue Aufgabe ein. ")
    myTasks.append(task)
    print("Deine Aufgabe wurde erfolgreich hinzugefügt.")

def viewTask():
    print("Meine To Do's")
    if len(myTasks) == 0:
        print("Noch keine Aufgaben vorhanden. Füge zuerst welche hinzu.")
    else:
        for index, task in enumerate(myTasks, 1):   # Tasks werden beginnend mit 1 nummeriert
            print(f"{index}. {task}")

def markAsCompleted():
    taskNumber = int(input("Gib die Nummer der Aufgabe ein, um sie als erledigt zu markieren. "))-1     # -1, da Python bei 0 zu zählen beginnt
    if 0 <= taskNumber <= len(myTasks):
        completed_tasks = myTasks.pop(taskNumber)   # pop anstatt remove, da Task gespeichert und zu anderer Liste hinzugefügt
        tasksDone.append(completed_tasks)
        print("Die Aufgabe ist als erledigt gekennzeichnet.") 
    else:
        print("Gib eine gültige Aufgabennummer ein.")

def showCompletedTasks():
    print("Erledigte Aufgaben")
    if len(tasksDone) == 0:
        print("Noch keine Aufgaben erledigt.")
    else:
        for index, task in enumerate(tasksDone, 1):
            print(f"{index}. {task}")

def changeTaskText():
    taskNumber = int(input("Gib die Nummer der Aufgabe ein, um den Text zu ändern. ")) - 1
    if 0 <= taskNumber < len(myTasks):
        new_text = input("Gib den neuen Text für die Aufgabe ein. ")
        myTasks[taskNumber] = new_text
        print("Der Text der Aufgabe wurde erfolgreich geändert.")
    else:
        print("Gib eine gültige Aufgabennummer ein. ")


def main():
    while True:
        menu()
        choice = input("Gib deine Auswahl ein (1-5). ")
        if choice == "1":
            addTask()
        elif choice == "2":
            viewTask()
        elif choice == "3":
            markAsCompleted()
        elif choice == "4":
            showCompletedTasks()
        elif choice == "5":
            changeTaskText()
 
if __name__ == "__main__":
    main()