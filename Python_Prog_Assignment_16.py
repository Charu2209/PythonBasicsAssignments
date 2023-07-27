# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def stutter(input):
    '''This function returns the stutter string.\n
    Example: stutter("incredible") ➞ "in... in... incredible"\n
    Note: Input should be in lower case and atleast 2 characters long.
    '''

    if len(input)==2:
        print(input)
    else:
        print(input[0:2]+"... "+input[0:2]+"... "+input) 

stutter("incredible")

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def radians_to_degree(angle):
    '''This function converts the angle from radians to degrees'''

    return round(angle*57.2958,1)
print("angle in degrees : {}".format(radians_to_degree(20)))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def iscurzon(num):
    '''Check whether the number is curzon or not.'''

    if((((2**num)+1))%(2*num+1)==0):
        return True
    else:
        return False

print("Number is curzon : ", iscurzon(10))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

import math
def areaHexagon(side):
    '''This function returns the area of the hexagon provided the length of the side.'''

    return (3*math.sqrt(3)* side**2)/2

print("Area of the hexagon is : ", round(areaHexagon(2),1))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")
def binary(decimalNum):
    '''This function converts the binary number to decimal. '''

    return "{0:b}".format(decimalNum)

print("Binary representation is : ",binary(4))  




