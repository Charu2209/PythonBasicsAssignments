# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def factorial(num):
    '''This function calculates the factorial of a number.\n
    Parameters:
    num(int)'''

    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

print("Factorial of a number is : ",factorial(0))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def multiplicationTable(num):
    for i in range(1,11):
        print("{} * {} = {}".format(num,i,num*i))

multiplicationTable(2)

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def fibonacci(num):
    num1=0
    num2=1

    if(num<0):
        print("Enter a positive number")
    elif(num==1):
        print(num1)
    elif(num==2):
        print(num1,num2)
    else:
        
        print(num1,num2,end=' ')
        for i in range(0,num-2):
            temp=num2
            num2+=num1
            num1=temp
            print(num2,end=' ')

fibonacci(8)

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def isArmstrong(num):
    sum=0
    temp=num
    while(num>0):
        sum+=(num%10)**3
        num=num//10

    if(temp==sum):
        return True
    else:
        return False
    
if(isArmstrong(3)):
    print('Armstrong number.')
else:
    print('Not an Armstrong number.')

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def armstrongInInterval(start,end):
    '''This function finds the armstrong number in an interval.\n
    Parameters:\n
    start(int)-Start of the interval\n
    end(int)-End limit of the interval'''
    flag=False
    for i in range(start,end):
        if(isArmstrong(i)):
            print(i,end= ' ')
            flag=True

    if(flag!=True):
        print('No Armstrong number within the range.')

armstrongInInterval(2,400)

# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")

def sumNaturalNo(start,end):
    '''This function finds the sum of natural numbers within the range.\n
    Parameters:\n
    start(int)-start of the range
    end(int)-end of the range'''

    sum=0
    if start<1:
        for i in range(1,end):
            sum+=i
    else:
        for i in range(start,end):
            sum+=i

    return sum

print("sum of natural number is : {}".format(sumNaturalNo(1,1)))

       
    