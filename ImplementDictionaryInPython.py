# Implement Dictionary in Python
# EasyAccuracy: 31.99%Submissions: 7K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# You are familiar with most of the properties of dictionary in Python. Add some more info about dictionary through dictionary formatting and deleting key value pair.

# Formatting:
# hash = {}
# hash['Geeks'] = 5
# hash['geeksforgeeks'] = 13
# s = ("Count of characters is " + hash[Geeks] + " in " + key)             

# # results in: Count of characters is 5 in GfG

# Deleting:
# dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
# del dict['c']         

# # delete entry for 'c'

# Let's get this into head by solving a question. Given list of some students in a list and their corresponding marks in another list.The task is to do some operations as described below:
# a. i key value: inserts key and value in dictionary, and print 'Inserted'.
# b. d key: delete the entry for given key and print 'Deleted' if key to be deleted is present, else print '-1'.
# c. key: print marks of given key in statement as "Marks of student_name is : marks". If key is not present print '-1'.

 

# Example:

# Input:
# 5
# i geeks 100
# i for 200
# d geeks
# i geeks 300
# p geeks

# Output:
# Inserted
# Inserted
# Deleted
# Inserted
# Marks of geeks is 300

# Explanation:
# For first four queries, insert
# and del operation happens, 
# correspondingly Inserted and
# Deleted is printed. For last
# query, marks of geeks is printed.
# Constraints:
# 1 <= N <= 104
# 1 <= marks <= 104

# Your Task:
# The task is to complet the function insert_dict(), del_dict() and print_dict() which should do the operations as required.

# soln:

#User function Template for python3

# insert into dictionary
def insert_dict(key, value, dict):
    
    # Your code here
    dict[key]=value
    

# deleting from dictionary
def del_dict(key, dict):
    
    # Your code here
    
    if key in dict:
        del dict[key]
    
    
    

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    
    if key in dict:
        print("Marks of "+str(key)+" is "+str(dict[key]))
        return dict
    else:
        return False
    
    
    