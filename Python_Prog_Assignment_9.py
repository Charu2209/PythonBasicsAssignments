# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def isDisarium(num):
    '''This function checks whether the number is Disarium or not.'''

    pos = len(str(num))
    sum=0
    num_copy=num
    while(num_copy!=0):
        sum+=(num_copy%10)**pos
        num_copy=num_copy//10
        pos-=1

    if sum==num:
        return True
    else:
        return False

print(" Disarium Number : ", isDisarium(134))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def allDisarium(start,end):
    '''This function prints all the Disarium number within the range'''
    for i in range(start,end):
        if isDisarium(i):
            print(i,end = ' ')

allDisarium(1,100)

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def isHappy(num):
    '''This function checks whether a number is happy number or not.'''

    st=set()
    num_copy=num
    sum=0
    flag=0

    while(True):
        
        st.add(num_copy)
        sum=0
        while(num_copy!=0):
            sum+=(num_copy%10)**2
            num_copy = num_copy//10
        
        num_copy=sum

        if(sum==1):
                return True
        elif(sum in st):
            return False

    return True
        
print('Number is Happy Number : ', isHappy(14))
        

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def allHappyNo(start,end):
    '''This function prints all the Disarium number within the range'''
    for i in range(start,end):
        if isHappy(i):
            print(i,end = ' ')

allHappyNo(1,100)


# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def isHarshad(num):
    '''This function checks whether a number is Harshad or not.'''

    num_copy=num
    sum=0

    while(num_copy!=0):
            sum+=(num_copy%10)
            num_copy = num_copy//10
    if num%sum==0:
        return True
    else:
        return False

print("Number is Harshad Number : ",isHarshad(19))

# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")

def allHarshadNo(start,end):
    '''This function print all Harshad numbers within the provided range.'''

    for i in range(start,end):
        if isHarshad(i):
            print(i,end = ' ')

allHarshadNo(1,100)

