"""
Program goals:
1. Add items to list (ints)
2. Offer the user a choice of actions
3. Pull the values stored at specific indexes
4. Convert input to INTSs

"""

def mainprogram():
    myList = []
    print("Hello, there! Let's work with lists!")
    print("Please choose from options the following options. Type the number of the choice")
    choice = input("1, Add to a list, 2. Return a vaule at a list  ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
    

def addToList():
    print("Adding to a list: Great choice!")
    newItem = input("Type an interger here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def indexValues():


if __name__ =="_main_":
    mainProgram()
