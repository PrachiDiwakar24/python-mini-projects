# Library Management System

books = ["Python Basics", "Machine Learning", "Data Science"]
issued_books = []

while True:
    
    print("\n--- Library Management System ---")
    print("1. View Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(books) == 0:
            print("No books available.")

        else:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)

    elif choice == "2":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "3":
        book = input("Enter book name to issue: ")

        if book in books:
            books.remove(book)
            issued_books.append(book)
            print("Book issued successfully!")

        else:
            print("Book is not available.")

    elif choice == "4":
        book = input("Enter book name to return: ")

        if book in issued_books:
            issued_books.remove(book)
            books.append(book)
            print("Book returned successfully!")

        else:
            print("This book was not issued.")

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice!")