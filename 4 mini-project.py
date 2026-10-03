score = 0

print("---Welcome to the Quiz Game---")
print("Answer the following questions:\n")

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1

else:
    print("Wrong! The correct answer is delhi.")

answer = input("2. Which language are we using in this project? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1

else:
    print("Wrong! The correct answer is Python. ")

answer = input("3. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1

else:
    print("Wrong! The correct answer is 7.")

answer = input("4. Which planet is known as the Red Planet? ")

if answer.lower() == "mars":
    print("Correct!")
    score += 1

else:
    print("Wrong!The correct answer is Mars.")

answer = input("5. How many months are there in a year? ")

if answer == "12":
    print("Correct!")
    score += 1

else:
    print("Wrong!The correct answer is 12.")

print("\n-----Quiz Completed-----")
print("Your score is:", score, "out of 5")