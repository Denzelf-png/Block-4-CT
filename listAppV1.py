"""
Program goals:
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action in a while loop

"""
myList = []
 
def mainProgram():
    #Build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from options the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. Return a vaule at a list,
3. Random Search
4. Quit  """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch()
        else:
            break
    

def addToList():
    print("Adding to a list: Great choice!")
    newItem = input("Type an interger here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def randomSearch():
    print(" oH iM sO rAnDom!!!")
    print(myList[random.randit(0, len(myList)-1)])

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPos)])
    
if __name__ =="__main__":
    mainProgram()
