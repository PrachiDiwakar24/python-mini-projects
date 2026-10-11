# Online Shopping Cart System.

products = {
    "1": ("Notebook", 50),
    "2": ("Pen", 10),
    "3": ("School Bag", 500),
    "4": ("Water Bottle", 150)
}

cart = []

while True:

    print("\n--- Shopping Cart ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        for key, (name, price) in products.items():
            print(key, name, "- ₹", price)

    elif choice == "2":
        product_id = input("Enter product number: ")

        if product_id in products:
            cart.append(products[product_id])
            print("Product added to cart!")

        else:
            print("Product not found.")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")

        else:
            total = 0
            for name, price in cart:
                print(name, "- ₹", price)
                total += price

            print("Total: ₹", total)

    elif choice == "4":
        total = sum(price for name, price in cart)
        
        print("Your total bill is ₹", total)
        print("Thank you for shopping!")
        break

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")