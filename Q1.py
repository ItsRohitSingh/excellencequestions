#Question1 -
# Use python lists and make an list of numbers.
# Write a function which returns sum of the list of numbers



def addlist(lst):
    sum = 0
    for i in lst:
        sum+=i
        
    return sum
    

lst = [int(x) for x in input("Enter the list of numbers with (space seperated values) : ").split(sep=' ')]

print("The sum of all the numbers in the given list is :", addlist(lst))