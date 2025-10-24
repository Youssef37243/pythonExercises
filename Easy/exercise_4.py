# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean.

mylist = list(range(5))

def my_list(mylist, checkNum):
    if checkNum in mylist:
        return True
    
    else:
        return False
    
userNum = int(input("Enter a number to check: "))

if(my_list(mylist, userNum)):
    print(f'{userNum} is in the list!')

else:
    print(f'{userNum} is not in the list!')