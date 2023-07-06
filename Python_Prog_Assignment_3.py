# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def check(num):
    '''This function checks whether a number is positive, negative,zero \n
    Parameters:\n
    Num(int)\n'''
    if(num==0):
        print("Number is zero.")
    elif(num<0):
        print("Number is negative.")
    else:
        print("Number is positive.")

check(-4)

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def isOddEven(num):
    '''This function checks whether a number is odd or even.\n
    Parameters:
    num(int)'''

    if(num%2==0):
        print("Number is even.")
    else:
        print("number is odd.")

isOddEven(1)

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def isLeapYear(year):
    '''This function checks whether the year is leap or not.\n
    Parameters:\n
    year(int)'''

    if( (year%400==0 and year%100==0) or (year%4==0 and year%100!=0)):
        print("Year is leap year")
    else:
        print("Year is not leap year")

isLeapYear(2004)

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def isPrime(num):
    '''This function checks whether a number is prime or not.\n
    Parameters:\n
    num(int)'''

    if(num==1):
        return False
    elif(num==2):
        return True
    else:
        for i in range(2,(num//2)+2):
            if(num%i==0):
                return False
            else:
                return True

if(isPrime(5)):
    print('Prime number')
else:
    print('Not a Prime number')

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def primeNumbers():
    '''This function prints all the prime numbers between 1-10000.\n
    '''
    for i in range(0,10000):
        if(isPrime(i)):
            print(i, end=' ')

primeNumbers()