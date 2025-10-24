# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. For practice, 
# write this code inside a function.

a = [5, 10, 15, 20, 25]

def first_Last(a):
    new_a = [x for x in a if x == a[0] or x == a[-1]]
    return new_a

new_a = first_Last(a)
print(f'New list is: {new_a}')