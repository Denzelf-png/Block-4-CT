Section 1 How the program works
The program uses the user inputs to direct to diffrent function throuhout the program.The reason for creating two list is because the function requires a specfic list in order to fuction properly, if these requirments arent meant they will result in erorrs in your code.


Section 2 Binary Search

Binary search algorthims uses in interers by for searching an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

Recursive Binary search 
is an implementation of the binary search algorithm that uses recursive method calls (instead of iteratively searching for the item within a single method call).It is a process, always applied to a function and iteration is applied to the set of instructions which we want to get repeatedly executed.  a Recursive algorithm, a module (function) calls itself again and again till the base condition(stopping condition) is satisfied. So it takes a list and spilts into two sides,it uses the user choice to search for an integer from the list a directly chooses the number choosen by the users choice.


Iterative Binary search 
If number at position mid equal to key or target element then the control returns index of mid element by printing that the number has been found along with the index at which it was found. This search algorthim is very similar to Recursive because recursive search for the interger in loops until if find the number chooen while on the other hand, An Iterative algorithm will use looping statements such as for loop, while loop or do-while loop to repeat the same steps.


Section 3 Changes/Added code

My added code was an "def all(iterable):"
"""
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

this function shows that for each itrative elemnts return as true if its not an iterative elemnt is will return as false.

I also added a copy list fuction this will show the user wiether the list was copied or not.
def copyList():
    print("List is copied!")

I also added a function that will copy the list
def copyList():
    print("List is copied!")