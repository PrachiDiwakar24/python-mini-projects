# hotel menu billing system

menu = {

    'pizza': 90,
    'coffee': 80,
    'burger':100,
    'pasta':70,
    'salad':70,
    'tea':50,
}

print("....WELCOME TO PYTHON HOTEL....")

print("pizza:Rs90\ncoffee:Rs80\nburger:Rs100\npasta:Rs70\nsalad:Rs70\ntea:Rs50")

order_total = 0

item_1 = input("enter the name of the item you want to order :")

if item_1 in menu:

    order_total += menu[item_1]

    print(f"your item {item_1} has been added to your order.")

else:

    print(f"ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item?(yes/no) :")

if another_order == "yes":

    item_2 = input("enter the name of second item :")

    if item_2 in menu:

        order_total += menu[item_2]

        print(f"ordered item {item_2} has been added to order")

    else:

        print(f"ordered item {item_2} is not availabel yet!")

print(f"the total ammount of item is {order_total} .")