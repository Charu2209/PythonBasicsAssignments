# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def LCM(num1,num2):
    '''This function finds the LCM of 2 numbers.\n
    '''

    if(num1>num2):
        greater=num1
    else:
        greater=num2

    while(True):
        try:
            if(greater%num1==0 and greater%num2==0):
                return greater
        except ZeroDivisionError:
            return 0
        greater+=1
   
print("LCM is : {}".format(LCM(0,1)))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def HCF(num1,num2):
    if(num1>num2):
        greater=num1
        smaller=num2
    else:
        greater=num2
        smaller=num1

    while(True):
        try:
            if(greater%smaller==0):
                return smaller
            temp=smaller
            smaller=greater%smaller
            greater=temp
        except ZeroDivisionError:
            return greater
    
print("HCF is : {}".format(HCF(0,5)))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def convertDecimal(n):
    '''This function converts the decimal number to Binary,Octal and Hexadecimal'''
    print('Binary number is : ', bin(n).replace("0b",""))
    print('Octal number is : ', oct(n))
    print("Hexadecimal number is : {0:x}".format(n))

convertDecimal(69)

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def findASCII(char):
    '''This function returns the ASCII value of a character.'''
    return ord(char)

print("ASCII value of character is : ", findASCII('g'))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")
def calculator(num1,num2):

    print("Enter an operation to perform : +,-,/,*")
    op = input()

    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='/':
        try:
            return num1/num2
        except Exception as e:
            return e
    elif op=='*':
        return num1*num2
    
print("Solution is : {}".format(calculator(5,7)))
    



