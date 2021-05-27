# Question2 -
# Setup a dict structure like this in python
# Dict1: (this is a key, value pair of user id and username)
# {
#    “1” : “name1”,
#    “2” : “name2”,
#    “3” : “name3”
# } etc.. 
# Dict2: (this is a key value pair of user id and exam score) 
# {
#    “1” : 50,
#    “2” : 60
#    “3” : 70
# }
# These are just sample data assume there are hundreds of users 

# Write a function in python in python, which will return maximum i.e function should return dictionary like
# {
#   “3” : 70
# }



def maxdict(Dict2):
    max_val = 0
    for i in Dict2.values():
        if i > max_val:
            max_val = i
            
    max_key_index = list(Dict2.values()).index(max_val)
    max_key = list(Dict2.keys())[max_key_index]
    
    Dict3 = {max_key : max_val}
    
    return Dict3

Dict2 = {1:10, 2:20, 3:80, 5:60, 10:100}
print(maxdict(Dict2))