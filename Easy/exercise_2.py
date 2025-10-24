# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd number 
# react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message. 
# Ask the user for two numbers: one number to check (call it num) and one number to divide 
# by (check). If check divides evenly into num, tell that to the user. If not, print a different 
# appropriate message.

def randomNum(randNum):
    if randNum % 4 == 0:
        print("You choose a number divisible by 4😃")

    elif randNum % 2 == 0:
        print("You choose an even number😃")

    else:
        print("You choose an odd number😃")

randNum = int(input("Enter a random number: "))
randomNum(randNum)

def checkNum(num, check):
    if num % check == 0:
        print(f"{num} is divisble by {check} 😃")
    
    else:
        print(f"{num} is not divisble by {check} 😔")

num = int(input("Enter a num: "))
check = int(input("Enter check: "))
checkNum(num, check)