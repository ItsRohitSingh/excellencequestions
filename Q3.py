# Question 3
# Assume we have list like this
# [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
# Basically a list of zero’s and one’s.
# Write a python function to the number of maximum consecutive  one’s present in the array. 
# E.g output for the above array would be 4



def countones(lst):
    count = 0
    i = 0 
    maxcount = 0
    l = len(lst)
    while i<l:
        if lst[i] == 1:
            count += 1
            
        else:
            if count > maxcount:
                maxcount = count

            count = 0
        i+=1
        
    return maxcount

lst = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
print("The maximum consecutive one's present in the array is :", countones(lst))