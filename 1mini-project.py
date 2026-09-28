# guess the number


import random

target = random.randint(1,100)

while True:
     userchoice = input("guess the target or quit(Q):")

     if(userchoice == "Q"):
          break
     
     userchoice = int(userchoice)

     if(userchoice == target):
          print("success : correct guess!!")
          break
     
     elif(userchoice < target):
        print("your number was too small. take a bigger guess...")

     else:
      print("your number was too big. take a smaller guess...")
print("------game over------")
