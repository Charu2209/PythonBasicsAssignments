# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

import functools

def sumListEl(list1):
    '''This function finds the sum of all the elements of a list.'''
    return functools.reduce(lambda a,b: a+b,list1)

print("Sum of List Elements is : {}".format(sumListEl([1,2,3,4,5])))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def mulListEl(list1):
    '''This function multiplies the all the elements of a list.'''
    return functools.reduce(lambda a,b:a*b,list1)

print("Multiple of List Elements is : {}".format(mulListEl([1,2,3,4,5])))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def smallestInList(list1):
    '''This function finds the smallesr elements in a list.'''
    return functools.reduce(lambda a,b: a if a<b else b, list1)

print("Smallest of the List Elements is : {}".format(smallestInList([1,2,3,4,5])))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def largestInList(list1):
    '''This function finds the smallesr elements in a list.'''
    return functools.reduce(lambda a,b: a if a>b else b, list1)

print("Largest of the List Elements is : {}".format(largestInList([1,2,3,4,5])))

# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")

def nthLargestInList(list1,n):
    '''This function finds the nth largest elements in a list.'''
    list1.sort()
    return list1[-n]

print(" nth Largest of the List Elements is : {}".format(nthLargestInList([1,2,3,4,5],4)))

# Question 7
print("\n")
print("Question 7 Solution")
print(120*"-")

def evenNoInList(list1):
    '''This function finds the even elements in a list.'''
    return [a for a in list1 if a%2==0]

print("Even elements of the List Elements are : {}".format(evenNoInList([1,2,3,4,5])))

# Question 8
print("\n")
print("Question 8 Solution")
print(120*"-")

def oddNoInList(list1):
    '''This function finds the odd elements in a list.'''
    return [a for a in list1 if a%2!=0]

print("Odd elements of the List Elements are : {}".format(oddNoInList([1,2,3,4,5])))

# Question 9
print("\n")
print("Question 9 Solution")
print(120*"-")

def removeEmptyList(list1):
    '''This function removes empty list from the list of list.'''
    return [a for a in list1 if len(a)!=0]

print("List after removing empty list is : {}".format(removeEmptyList([[1,2,3,4,5],[],[1]])))

# Question 10
print("\n")
print("Question 10 Solution")
print(120*"-")

def cloneList(list1):
    '''This function creates the copy of a list.'''
    return [a for a in list1]

print("Copied list is : {}".format(cloneList([1,2,3,4,5])))

# Question 11
print("\n")
print("Question 11 Solution")
print(120*"-")

def countListEl(list1,ele):
    '''This function finds the occurence of element in a list.'''
    count=0
    for i in list1:
        if i==ele:
            count+=1

    return count

print("Occurence of the list element is  : {}".format(countListEl([1,2,3,4,5,5,5],5)))



