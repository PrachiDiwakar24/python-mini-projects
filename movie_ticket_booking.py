#  Movie Ticket Booking System

movies = {
    "1": ("Avengers", 150),
    "2": ("Dangal", 120),
    "3": ("3 Idiots", 100)
}

print("--- Movie Ticket Booking ---")

print("\nAvailable Movies:")

for number, movie in movies.items():
    print(number + ".", movie[0], "- ₹", movie[1])

choice = input("\nSelect a movie: ")

if choice in movies:
    
    movie_name, price = movies[choice]

    tickets = int(input("Enter number of tickets: "))

    total = price * tickets

    print("\n--- Booking Details ---")
    print("Movie:", movie_name)
    print("Tickets:", tickets)
    print("Total Price: ₹", total)
    print("Booking successful!")

else:
    print("Invalid movie choice!")