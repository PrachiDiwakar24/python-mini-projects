#  Random Quote Generator...

import random

quotes = {

    "Motivation": [
        "Believe in yourself.",
        "Small steps lead to big results.",
        "Never give up on your dreams."
    ],
    "Study": [
        "Learning never stops.",
        "Consistency is the key to success.",
        "Focus today, shine tomorrow."
    ],
    "Success": [
        "Success comes from hard work.",
        "Dream big and take action.",
        "Every failure teaches a lesson."
    ]
}

favorites = []

def generate_quote():
    print("\nCategories:")
    categories = list(quotes.keys())

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    try:
        choice = int(input("Choose a category: "))

        if choice not in range(1, len(categories) + 1):
            print("Invalid category!")
            return

        category = categories[choice - 1]
        quote = random.choice(quotes[category])

        print(f"\n[{category}]")
        print(f'"{quote}"')

        save = input("Add to favorites? (yes/no): ").lower()

        if save == "yes":
            if quote not in favorites:
                favorites.append(quote)
                print("Quote added to favorites!")

            else:
                print("Already in favorites!")

    except ValueError:
        print("Please enter a valid number.")

def show_favorites():
    print("\n=== Favorite Quotes ===")

    if not favorites:
        print("No favorite quotes saved yet.")

    else:
        for i, quote in enumerate(favorites, 1):
            print(f"{i}. {quote}")

while True:

    print("\n=== Smart Quote Generator ===")
    print("1. Generate a quote")
    print("2. View favorites")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_quote()

    elif choice == "2":
        show_favorites()

    elif choice == "3":
        print("Keep learning and stay inspired!")
        break
    
    else:
        print("Invalid choice. Try again.")