import random

#NOTES FROM DO NOW:
#1. Work with integers
#2. Random number generator
#3. A way to give commands(controls)

#FEATURES TO ADD:
#1. How to keep the program running until i quit
#2. Use numberOfRolls variable to show multiple die rolls
#3. Add roll totaling features (sum/highest/lowest)
#4. More human interface

myRolls= []


def diceEngine():
    #a while loop will run forever until it's deliberately exited
    while True:
        dieType = input("How many sides should the die have?  ")
        numberOfRolls = input("How many times do you want to roll?   ")
        print("*Roll die*")


        #use a loop to iterate through the number of rolls
        for x in range(0, int(numberOfRolls)):
            myRolls.append(random.randint(1, int(dieType)))
                           
        print("Here are your rolls: ()".format(myRolls))
        print("Your roll total was: ()".format(sum(myRolls)))
        print("Your highest roll was: ()".format(max(myRolls)))
        print("Your lowest roll was: ()".format(min(myRolls)))

        #add a way to exit the loop
        rollAgain = input("Would you like to roll again? y / n?   ")
        if rollAgain == "n":
            break
        #add a way to clear the list for the next roll
        clearList = input("Do you want me to clear your list of rolls? y / n   ")
        if clearList == "y":
I like how the arrows show the direction of the trend and how you have the descriptions. Maybe try to make the description more concise            myRolls.clear()
            
if __name__== "__main__":
    diceEngine()

