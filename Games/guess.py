import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the target or Quit(Q): ")
    if(userchoice == "Q"):
        print("Number was",target)
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success: Correct Guess !!")
        break
    elif(userchoice < target):
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")

print("----GAME OVER-----")
