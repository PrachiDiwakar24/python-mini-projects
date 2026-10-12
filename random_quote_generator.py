#  Random Quote Generator...

import random

quotes = [

    "Believe in yourself.",
    "Never stop learning.",
    "Small steps lead to big results.",
    "Dream big and work hard.",
    "Every day is a new opportunity.",
    "Success comes from consistency.",
    "Learn from your mistakes.",
    "Your future depends on what you do today .",
    "Stay curious and keep growing.",
    "Great things take time."
]

def generate_quote():

    quote = random.choice(quotes)
    print("\nYour Random Quote:")
    print('"' + quote + '"')

print("=== Random Quote Generator ===")

while True:

    print("\n1. Generate a quote")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_quote()

    elif choice == "2":
        print("Keep learning and stay motivated!")
        break
    
    else:
        print("Invalid choice. Please try again.")