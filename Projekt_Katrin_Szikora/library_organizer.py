my_profile_info = []
book_collection = []

def menu():
    print("\nYour Library Organizer")
    print("1. Create Profile")
    print("2. Manage Books")
    print("3. Rate Books")
    print("4. View Ratings")
    print("5. Discover Page")
    print("6. Move Books")
    print("7. Sort Books")
    print("8. Show Profile")
    print("9. Exit Library Organizer")

# Random Quote Generator

import random

def random_quote():
    file = open("quotes.txt")
    quotes = file.readlines()
    file.close()
    return random.choice(quotes)

# Profile

def create_profile():

    print("\nIt's time to create your Profile. Fill in the requests below and get right into it.")

    profile_fields = [
        ("first name", "Enter your first name: "),
        ("last name", "Enter your last name: "),
        ("bio", "Enter a short Bio: "),
    ]

    for index, (field, prompt) in enumerate(profile_fields, start=1):
        user_input = input(f"{index}. {field.capitalize()}: ")
        my_profile_info.append(user_input)

    save_my_profil_info(my_profile_info)

    available_genres = ["Classics", "Fantasy", "Non-Fiction", "Romance", "History", "Thriller", "Philosophy", "Psychology"]
    print("\nAvailable Genres:")
    for index, genre in enumerate(available_genres, start=1):
        print(f"{index}. {genre}")

    favorite_genres = input("\nEnter the Numbers of your favorite Genres: ")

    favorite_genres = [int(index) for index in favorite_genres.split(",")]

    favorite_genres = ', '.join([available_genres[index - 1] for index in favorite_genres])
    my_profile_info.append(favorite_genres)
    save_my_profil_info(my_profile_info)

def save_my_profil_info(my_profile_info):          # Inhalt des Arrays my_profile_info wird im File my_profile_info.txt gespeichert
    file = open("my_profile_info.txt", "w")
    for item in my_profile_info:
        file.write(item + "\n")
    file.close()

def load_profil_info():       # Profilinfo über Neustart hinweg speichern
    my_profile_info = []
    file = open("my_profile_info.txt", "r")
    my_profile_info = file.readlines()
    file.close()
    return my_profile_info

# Manage Books

def manage_books():
    while True:
        print("\nManage Books Options:")
        print("1. Add a Book")
        print("2. View Books by Shelf")
        print("3. Back to Main Menu")

        choice = input("Select your option (1-3): ")
        print() # Leerzeile

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books_by_shelf()
        elif choice == "3":
            break
        else:
            print("Invalid input. Please choose an option from 1 to 3.")

def add_book():
    title = input("Enter the title of the book: ")
    author_first_name = input("Enter the first name of the author: ")
    author_last_name = input("Enter the last name of the author: ")

    print("\nSelect the shelf:")
    print("1. Plan to Read")
    print("2. Reading")
    print("3. Currently Read")

    shelf_choice = input("Enter the number of the shelf (1-3): ")
    shelves = ["Plan to Read", "Reading", "Currently Read"]

    shelf_choice = int(shelf_choice)
    if 1 <= shelf_choice <= 3:
        shelf = shelves[shelf_choice - 1]
        with open("book_collection.txt", "a") as file:
            file.write(f"{title} by {author_first_name} {author_last_name} - Shelf: {shelf}\n")
            print("Book successfully added.")
    else:
        print("Invalid shelf number. Please enter a number between 1 and 3.")

def view_books_by_shelf():
   with open("book_collection.txt", "r") as file:
        books = file.readlines()
        if not books:
            print("No books available.")
        else:
            print("Book Collection:")
            for book in books:
                print(book.strip())

# Rate Books

def rate_books():
    book_title = input("\nEnter the title of the book: ")
    author = input("Enter the author of the book: ")
    rating = input("Enter your rating for the book (1-5): ")

    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            print("Invalid rating. Please enter a number between 1 and 5.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    with open("book_ratings.txt", "a") as file:
        file.write(f"{book_title} by {author} - Rating: {rating}\n")

    print("Rating successfully saved.\n")

# View Ratings

def view_ratings():
    with open("book_ratings.txt", "r") as file:
        ratings = file.readlines()
        if not ratings:
            print("\nNo ratings available.\n")
        else:
            print("\nBook Ratings:")
            for rating in ratings:
                print(rating.strip())

# Discover Page
    
import random

def discover_page():
    print("\nDiscover Page:\n")
    
    recommended_book = get_random_book()
    if recommended_book:
        print(f"Recommended Book: {recommended_book}")
        
        while True:
            response = input("Do you want another recommendation? (yes/no): ")
            print() # Leerzeile
            if response.lower() == "yes":
                recommended_book = get_random_book()
                if recommended_book:
                    print(f"Recommended Book: {recommended_book}")
                else:
                    print("No more recommendations available.")
                    break
            elif response.lower() == "no":
                print("Discover Page closed.\n")
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

def get_random_book():
    file = open("recommended_books.txt")
    books = file.readlines()
    file.close()
    return random.choice(books)

# Move Books
        
def move_book():
    print("\nMove Book Options:")
    print("1. Move from Plan to Read to Reading")
    print("2. Move from Reading to Currently Read")
    print("3. Back to Main Menu")

    choice = input("\nSelect your option (1-3): ")

    if choice == "1":
        move_book_between_shelves("Plan to Read", "Reading")
    elif choice == "2":
        move_book_between_shelves("Reading", "Currently Read")
    elif choice == "3":
        return
    else:
        print("Invalid input. Please choose an option from 1 to 3.")

def move_book_between_shelves(source_shelf, target_shelf):
    with open("book_collection.txt", "r") as file:
        books = [book.strip() for book in file.readlines()]

    if not books:
        print("No books available.")
        return

    source_books = [book for book in books if f"Shelf: {source_shelf}" in book] # Filtern der Bücher im Quellregal

    if not source_books:
        print(f"\nNo books in the {source_shelf} shelf.\n")
        return

    print(f"\nSelect the book to move from {source_shelf}:")
    for index, book in enumerate(source_books, start=1):
        print(f"{index}. {book}")

    book_index = input("\nEnter the number of the book to move: ")

    book_index = int(book_index)
    if 1 <= book_index <= len(source_books):
        selected_book = source_books[book_index - 1]

        updated_book = selected_book.replace(f"Shelf: {source_shelf}", f"Shelf: {target_shelf}")
        books[books.index(selected_book)] = updated_book

        with open("book_collection.txt", "w") as file:
            for book in books:
                file.write(f"{book}\n")

        print("\nBook successfully moved.")
    else:
        print(f"\nInvalid book number. Please enter a number between 1 and {len(source_books)}.")

# Sort Books

def sort_and_display_books(sort_key):
    with open("book_collection.txt", "r") as file:
        books = [book.strip() for book in file.readlines()]

        if not books:
            print("No books available.")
            return

        if sort_key == "title":
            sorted_books = sorted(books, key=lambda book: book.split(" by ")[0] if " by " in book else "")
        else:
            print("Invalid sort key. Please choose 'title'.")
            return

        print("Sorted Book Collection:")
        for book in sorted_books:
            print(book)

def sort_books():
    print("\nSort Books:")
    print("1. Sort by Title")
    print("2. Back to Manage Books")

    choice = input("Select your option (1-2): ")
    print() #Leerzeile

    if choice == "1":
        sort_and_display_books("title")
    elif choice == "2":
        return
    else:
        print("Invalid input. Please choose an option from 1 to 2.")

def load_profil_info():
    my_profile_info = []
    try:
        with open("my_profile_info.txt", "r") as file:
            my_profile_info = file.readlines()
        if my_profile_info:
            print("\nYour Profile Information:")
            fields = ["First Name", "Last Name", "Bio", "Favorite Genres"]
            for field, value in zip(fields, my_profile_info):   # fields und my_profile_info paarweise ausgeben durch zip
                print(f"{field}: {value.strip()}")
    except FileNotFoundError:
        print("No profile information available.")

    return my_profile_info

def main():

    existing_profile = load_profil_info()

    print("\nQuote of the Day: ")     # Random Quote direkt am Beginn zeigen
    print(random_quote())

    while True:
        menu()
        choice = input("Select your choice (1-9). ")

        if choice == "1":
            if not existing_profile:
                create_profile()
                existing_profile = True
            else:
                print("\nProfile already exists. Choose another option.")
        elif choice == "2":
            manage_books()  
        elif choice == "3":
            rate_books()  
        elif choice == "4":
            view_ratings() 
        elif choice == "5":
             discover_page()
        elif choice == "6":
            move_book()
        elif choice == "7":    
            sort_books()
        elif choice =="8":
            load_profil_info()    
        elif choice == "9":    
            print("\nProgram terminated.")
            break
        else:
            print("\nInvalid input. Please choose an option from 1 to 9")

main()