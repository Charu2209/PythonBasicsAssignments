# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")


def hello_function():
    ''' this function prints the hello python statement'''
    print("Hello Pyhton!")

hello_function()

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")


def op_add_div(num1,num2):
    '''This function takes two arguments num1 and num2 and perform the addition and division operation 
    over them'''

    print("Result after addition operation is : ",num1+num2 )
    try:
        print("Result after division operation is : ",num1/num2 )
    except Exception as e:
        print("Error Occured!!")
        print(e)

op_add_div(4,0)

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def area_triangle(base,height):

    '''This function return area of triangle.
    Parameters:
    base(int) - argument 1
    height(int) - argument 2'''

    return 1/2*base*height

print("area of triangle is : ", area_triangle(3,4))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def swap(var1,var2):
    '''This functions swap 2 integer variables.
    Parameters:
    var1 and var2
    
    Returns :Swaped values'''

    var2,var1=var1,var2
    print("Varables after swapping : ",var1,var2)

swap('a','b')

# Question 4
print("\n")
print("Question 5 Solution")
print(120*"-")

import random

def generate_random():
    '''This function return the random number generated'''
    return random.random()

print("Random number is : ",generate_random())

