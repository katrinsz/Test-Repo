shopping_list = []

def menu():
    print("Meine Einkaufsliste")
    print("1. Produkt zur Einkaufsliste hinzufügen")
    print("2. Inhalt Einkaufsliste ausgeben")
    print("3. Komplette Einkaufsliste löschen")
    print("4. Produkt von Einkaufsliste löschen")
    print("5. Programm beenden")


def add_products(product, shopping_list):
    shopping_list.append(product)
    save_shopping_list(shopping_list)
    print(f"{product} wurde erfolgreich hinzugefügt.")


def show_shopping_list(shopping_list):
    print("Meine Einkaufsliste")
    if len(shopping_list) == 0:
        print("Deine Einkaufsliste ist leer. Füge zuerst etwas hinzu.")
        return
    else:
        for index, product in enumerate(shopping_list,1):
            print(f"{index}. {product}")

def delete_shopping_list(shopping_list):
    print("Bist du sicher, dass du deine komplette Einkaufsliste löschen willst?")
    decision_delete = input()
    if decision_delete == "ja":
        shopping_list.clear()
        save_shopping_list(shopping_list)
        print("Die Einkaufsliste wurde gelöscht.")
    else:
        print("Löschvorgang abgebrochen.")

def remove_product(delete_product, shopping_list):
    if delete_product in shopping_list:
        shopping_list.remove(delete_product)
        save_shopping_list(shopping_list)
        print(f"{delete_product} wurde erfolgreich entfernt.")
    else:
        print(f"{delete_product} ist nicht auf deiner Einkaufsliste")


def save_shopping_list(shopping_list):          # Inhalt des Arrays shopping_list wird im File shopping_list.txt gespeichert
    file = open("shopping_list.txt", "w")
    for item in shopping_list:
        file.write(item + "\n")
    file.close()

def load_shopping_list():       # Einkaufsliste über Neustart hinweg speichern
    shopping_list = []
    file = open("shopping_list.txt", "r")
    shopping_list = file.readlines()
    file.close()
    return shopping_list

def main():
    shopping_list = load_shopping_list()

    while True:
        menu()
        choice = input("Gib deine Auswahl ein (1-5). ")

        if choice == "1":
            product = input("Was möchtest du deiner Einkaufliste hinzufügen? ")
            add_products(product, shopping_list)
        elif choice == "2":
            show_shopping_list(shopping_list)
        elif choice == "3":
            delete_shopping_list(shopping_list)
        elif choice == "4":
            product = input("Welches Produkt möchtest du von deiner Einkaufsliste entfernen? ")
            remove_product(product, shopping_list)
        elif choice == "5":
            print("Programm beendet")
            save_shopping_list(shopping_list) 
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine Option von 1 bis 5.")

main()



