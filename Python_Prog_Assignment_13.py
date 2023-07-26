# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

import math

def calcultaValue():
    """This fi=unction returns the modified value of the input according the formula :
      Q = Square root of [(2 * C * D)/H]"""
    
    print("Enter the comma seperated numbers...")
    D=input()
    D_list = D.split(',')
    result=''

    for i in D_list:
        Q=int(math.sqrt((2*50*int(i)/30)))
        
        result+=str(Q)+','
    
    print("Output is  : ",result[0:-1])

calcultaValue()


# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def genMatrix():
    '''This function generates an X x Y Matrix whose element are rowNum*colNum.'''

    print("Input the value of X : ")
    X=input()

    print("Input the value of Y : ")
    Y=input()
    
    result = []

    for i in range(int(X)):
        list1=[]
        for j in range(int(Y)3):
            list1.append(i*j)

        result.append(list1)

    print("Matrix  : ", result)

genMatrix()

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def sortStr():
    '''This function sort the comma seperated string.'''

    print("Enter the comma seperated strung of words:")
    s=input().split(',')
    s.sort()
    print("Result : ", ','.join(s))

sortStr()

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def removeSortStr():
    '''This function removes dupicate and return the sorted string.\n
    Input: White Space seperated string.\n
    Note : This function treates uppercase and lower case differently'''

    print("Enter the string : ")
    print(' '.join(sorted(list(set(input().split(' '))))))
removeSortStr()

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def calculateLetterDigits(str):

    '''This fuction calculates the number of letters and digits in the input string.'''

    letter=0
    digit=0

    for i in str:
        if ord(i) in range(65,91) or ord(i) in range(97,123):
            letter+=1
        elif ord(i) in range(48,58):
            digit+=1
    
    print('LETTERS : ', letter)
    print('DIGITS : ',digit)

calculateLetterDigits('hello world! 123')

# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")

import re

def validatePass(passString):
    '''This function return the strings of password which are passing the criteria from the input string.'''

    result = []
    x=True

    for i in passString.split(','):

        while x:  
            if (len(i)<6 or len(i)>12):
                break
            elif not re.search("[a-z]",i):
                break
            elif not re.search("[0-9]",i):
                break
            elif not re.search("[A-Z]",i):
                break
            elif not re.search("[$#@]",i):
                break
            else:
                result.append(i)
                x=False
                break

    print(result)


validatePass('ABd1234@1,a F1#,2w3E*,2We3345')







    


    