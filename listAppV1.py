"""
Program goals:
1. Get input from the user (at multiple stages)
2. Convert some, but not all, inputs to ints from strings.
3. We need to provide the user with choices:
    a. Add more values to a list
    b. Return a value at a specific index position
4. Add search algorithms to program:
    a. Random Search
    b. Linear Search
    c. Binary Search (2 types)
    
"""

"""
import random imports the random module, which contains a variety of things to do with random number generation.
Among these is the random() function, which generates random numbers between 0 and 1. This allows you to then just call random() directly
"""
import random
myList = []
unique_list = []

"""
This is a greeting def is short for “define” def greet(person_name).
# begin definition puts "Hello, #{person_name}, nice to see you!" end # end definition greet("name") #=> Hello, name, nice to see you!
"""
def greet(name, msg="Good Morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello, Denzel Welcome to your List app!")

"""
This function defines the main program.We put a “while true” statement after this because a while true loop runs forever.
It is used to iterate over a block of code as long as the test expression (condition) is true.
"""
def mainProgram():
    #Build our while loop
    while True:
            print("Hello, there! Let's work with lists!")
            print("Please choose from the following options. Type the number of the choice")
            choice = input("""1. Add to a list,,
2. Add a bunch or numbers,
3.Get an item at an index
4. Sort List
5. Random Search
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List
10. Quit  """)
            """
           To obtain the user’s choice we first  have to use if, elif, and else statements. Each choice uses an “elif statement”  from the inputs of the users.
           Now we add a break statement. We use this because else statements don’t stop until it’s told to “break”.
            """
            if choice == "1":
                addToList()
            elif choice == "2":
                copyList()
            elif choice == "3":
                addABunch()
            elif choice == "4":
                indexValues()
            elif choice == "5":
                sortList(myList)
            elif choice == "6":
                randomSearch()
            elif choice == "7":
                linearSearch()
            elif choice == "8":
                binSearch = input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "9":                   
                binSearch = input("What number are you looking for?  ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position ()".format(result))
                else:
                    print("Your number is not found in that list, bud!")

            elif choice == "10":
                printLists()
            else:
                breakpoint
"""         
Def Add To List is defining the add to list function. First prints a statement “Adding to a list: Great choice!".
Now we add new item = = input ("Type an integer here!  ") this takes the user inputs of the numbers chosen before and adds it to a list.
Then myList.append(int(newItem)) adds a single integer  to the existing list of new items.
"""
def addToList():
    print("Adding to a list: Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    #we need to think about errors!
    
"""   
Def addABunch is defining the add a bunch function. First it prints a statement to the user "We're gonna add a bunch of numbers to your lists!".
Now we add Num to add which adds the numbers into the list the program asks the user what numbers they would like to add and  how high the user would like these numbers to go.
Now we add for x in range (0, int(num To Add)): this means for each value of x in range of the integer from the list of num to add.
Now we add myList.append(random.randint(0, int(numRange))) this adds  a single item to the existing list of num to a and  the random.randint method returns an integer number selected element from the specified range.
This number is from the user choice that is taken from the list num to add. Then it prints a statement to the user “your list is complete”.
"""
def addABunch():
    print("We're gonna add a bunch of numbers to your lists!")
    numToAdd = input("How many new integers would you like to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is complete!")
    
#
def sortList(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new, sorted list?  Y/N")
    if showMe.lower() =="y":
        print(unique_list)

"""
This function defines the copyList which copies a list and prints a statement to the user that the list is copied.
"""
def copyList():
    print("List is copied!")
    
"""   
Def Index Values is defining the index value function. First it prints a testament to the user "At what index position do you want to search?".
Next we add indexPos = input("Type an index position here: " which asks  the user to type an index position in the list.
Next we add print(myList[int(indexPos)]) this means it program prints my lists and adds the integer chosen into the index position.
"""
def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPos)])
"""
We created a variable called indexPos and stored the result of an input function inside it.
the value stored in indexPos into an integer (using the int() function) and used the variable to call a value at a specific index position.
Def Random Search is defining the random search function. First it prints a treatment to the user " oH i'M sO rAnDom!!!"
then it prints myList[random.randint(0, len(myList)-1)].) which imports random integers and chooses a number between 0 and the length of the list (board) minus 1.
"""
def randomSearch():
    print(" oH iM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])
"""        
First it prints a statement ("We're going to go through this list one item at a time!") to the user.
Then we search values and it asks for the user input by asking the user "what are you looking for? ".
Then we put x in range (len(myLists)): this means for each value of x in range of the length of 0 and the length of the list (myLists).      
"""
def LinearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("what are you looking for?    ")
    for x in range(len(myLists)):
        if myList[x] == int(searchValues):
         print("Your item is at index position {}".format(x))

my_list = []
if not len(my_list):
    print("the list is empty")
    
"""    
This defines the print list function which prints the list we then put an if statement stating if the length of the unique list is 0 that prints to the user my list.
then we have an else statement stating if anything else do you want the list sorted or unsorted.
"""
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or un-Sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
"""          
An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
Familiar examples of iterables include lists, tuples, and strings - any such sequence can be iterated over in a for-loop.
"""
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

"""
This function defines the recursive binary search.
Recursive binary search is an implementation of the binary search algorithm that uses recursive method calls (instead of iteratively searching for the item within a single method call).
Compare x with the middle element.If x matches with the middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recurse  for the right half.
Else (x is smaller) recur for the left half.
"""
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
        
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)
        
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

"""       
This function defines the iterative binary search, If x matches with the middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
Else (x is smaller) recur for the left half.
"""
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
            
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


"""
We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules are imported.
When the Python interpreter reads a file, the __name__ variable is set as __main__ if the module being run, or as the module's name if it is imported.           
"""
if __name__ =="__main__":
    greet("Denzel")
    greet("Denzel", "How do you do?")
    mainProgram()


