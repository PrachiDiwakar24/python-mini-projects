# Rock Paper Scissors Game

import random

print("🎮 Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()

if user not in choices:
    print("Invalid choice!")

else:
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (

        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")

    ):
        
        print("You won!")
        
    else:
        print("You lost!")