# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def kilometers_miles(kilometers):
    '''This function converts the kilometers to miles.
    Parameters:
    kilometeres(int)
    
    Return:
    Miles(int)'''
    return kilometers*0.621371

print("Kilometers after converting to miles : ",kilometers_miles(2) )

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def cel_to_fer(celsius):
    '''This function converts the celsius to fahrenheit.
    Parameters:
    Celsius(int)
    
    Return:
    Fahrenheit(int)'''
    return celsius*33.8

print("Celsius after converting to fahrenheit : ",cel_to_fer(2) )

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

import calendar

def disp_calendar(year,month):
    '''This function displays the calender
    Parameters:
    year(int)
    month(int)
    '''
    print(calendar.month(year,month))

disp_calendar(2023,1)

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

import cmath
def roots_quad_equation(a,b,c):

    ''' this function finds the 2 roots of an quadratic equation : ax**2+bx+c.\n
    Parameters:
    a(int) - a not equal to 0,\n
    b(int),\n
    c(int)
    '''
    
    if(a==0):
        print("Error: a connot be 0")
        return
    else:
        d=(b**2) - (4*a*c)
        root1 = (-b+cmath.sqrt(d))/2*a
        root2 = (-b-cmath.sqrt(d))/2*a
        print("Solutions of quadratic equations are : ", root1, root2)

roots_quad_equation(1,5,6)

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def swap(var1,var2):
    '''This functions swap 2 integer variables.
    Parameters:
    var1 and var2
    
    Returns :Swaped values'''

    var2,var1=var1,var2
    print("Varables after swapping : ",var1,var2)

swap('a','b')




