# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def list_operations(x,y,n):
    '''This function eturn an ordered list with numbers in the range(x,y) that are divisible 
    by the third parameter n.'''

    return [i for i in range(x,y+1) if i%n==0]

print(list_operations(15,20,7))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def simon_says(list1,list2):
    '''this function takes in two lists and returns True if the second list follows the first list
    by one element, and False otherwise.'''

    for i in range(1,len(list2)):
        if list2[i]!=list1[i-1]:
            return False
    return True

print(simon_says([1, 2, 3, 4, 5], [0,1,2,3,4]))


# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def society_name(list1):
    '''This function takes in a list of names and returns the name of the secret society ie. first alphabet 
    of each of the names in the list.'''

    result=''
    list1.sort()
    for i in list1:
        result+=i[0].upper()
    return result

print("Society name is : ", society_name(['Adam', 'Sarah', 'Malcolm']))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def is_isogram(s):
    '''This function checks whether the string is isogram or not.'''

    s=s.lower()

    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return False
    return True

print("String is isogram : {}".format(is_isogram('p')))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def is_in_order(s):
    '''This function checks whether the input is in order or not.'''
    temp=sorted(s)
    temp1= ''.join(temp)
    if s==temp1:
        return True
    return False

print("Is string in order : ",is_in_order("193"))


            

