# * Write a function that takes a list, a number, and a string as args. 
# * The string parameter should have a default value. 
# * In the function body, loop over the list and output the items.
# *  Use slice to loop through only the first n items in the array, where n = the value of the second argument.
# * Each item should be prefaced by value of the string argument
#    * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
# * Try it out! Execute the function both with and without passing in a value for the string parameter

def myFunc(myList, myNum, myWord="I don't like:"):
    for item in myList:
        print(item)
    for item in myList[:myNum]:
        print(f'{myWord} {item}')

myFunc(["apples", "bananas", "dogs", "avocados", "boating"], 3, "I like:")
myFunc(["apples", "bananas", "dogs", "avocados", "boating"], 3)
