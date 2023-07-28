# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def filter_list(l):
    ''' The function takes a list of strings and integers, and filters out the list so that it
    returns a list of integers only.'''

    return [i for i in l if type(i)!=str]
print(filter_list([1,2,3,'a','b',4]))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def add_indexes(l):
    '''This function wreturns the list but with each element's index in the list added to itself.
    '''

    return [ i+l[i] for i in range(len(l))]

print(add_indexes([0,0,0,0,0]))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

import math

def cone_volume(height,radius):
    '''This function calculates the volume of the cone.'''

    return round((1/3)*3.14*radius**2*height,2)

print(cone_volume(15,6))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def triangle(num):
    '''This function that gives the number of dots with its corresponding triangle number of the
        sequence.'''

    print("Result : ",int(num*(num+1)/2))

triangle(215)

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def missing_num(l):
    '''This function that takes a list of numbers between 1 and 10 (excluding one number) and
        returns the missing number.'''
    
    result = [i for i in range(1,11) if i not in l]
    print("Missing number is : ", result[0])

missing_num([1,2, 3, 4, 6, 7, 8, 9, 10])

