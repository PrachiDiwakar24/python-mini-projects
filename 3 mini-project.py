#  Digital Wallet Simulator 

balance = 1000

while True:

    print("\n--- Digital Wallet ---")
    print("1. Check Balance")
    print("2. Add Money")
    print("3. Spend Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to add: ₹"))
        balance += amount
        
        print("Money added successfully!")

    elif choice == "3":
        amount = float(input("Enter amount to spend: ₹"))

        if amount <= balance:
            balance -= amount
            print("Payment successful!")

        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using Digital Wallet!")
        break

    else:
        print("Invalid choice!")