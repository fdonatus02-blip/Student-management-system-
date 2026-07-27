def menu():
    print("\n=====LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add book")
    print("2. View books")
    print("3. search book")
    print("4. borrow book")
    print("5. return book")
    print("6. exit")


books = [
    {
        "title": "python basics",
        "author": "john",
        "year": 2024,
        "copies": 5
    }
] 
def add_book():
    title = input("title: ")
    author = input("author: ")
    year = int(input("year: "))
    copies = int(input("copies: "))

    book = {
        "title": title,
        "author": author,
        "year": year,
        "copies": copies
    }

    books.append(book)

    print("book added")


def view_books():
    for book in books:

        print("\ntitle:", book["title"])
        print("author: ", book["author"])
        print("year:", book["year"])
        print("copies:", book["copies"])

def search_book():
    search = input("enter title: ")

    for book in books:
        if book["title"].lower() == search.lower():
            print(book)
            return
        
    print("book not found")

def borrow_book():
    title = input("enter title")

    for book in books:

        if book["title"].lower() == title.lower():
            if book["copies"] > 0:
                book["copies"] -= 1
                print("book borrowed successfully")

            else:
                print("no copies available.")

def return_book():
    title = input("enter title")
    for book in books:
        if book["title"].lower() == title.lower():
            book["copies"] += 1
            print("book returned successfully")

            return
        print("book not found")

import json
def save_books():
    with open("books.json", "w") as file:
        json.dump(
            books,
            file,
            indent=4
        )

def load_books():
    global books
    try:
        with open("books.json", "r") as file:
            books = json.load(file)

    except:
        books = []
while True:
    menu()
    choice = input("enter choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        break
    else:
        print("invalid choice")