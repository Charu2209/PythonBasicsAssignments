# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def is_symmetric(num):

    '''This function checks whether the number is symmetric or not.'''
    s=str(num)
    if s==s[::-1]:
        return True
    return False

print("Number is symmetric : ", is_symmetric(12322))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def multiply_nums(s):
    '''This function takes the string of numbers and returns there product.'''

    list1=s.split(", ")
    prod=1
    for i in list1:
        prod*=int(i)
    return prod

print("Product is : ", multiply_nums("1, 2, 3, 4"))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def square_digits(num):
    '''This function squares every digit of the number.'''

    s=str(num)
    result=''
    for i in s:
        result+=str(int(i)*int(i))

    return int(result) 

print("Number after square digits: ",square_digits(9119))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def setify(list1):
    '''This function removes the duplicate and return the sorted list.'''

    set1=set(list1)
    return sorted(list(set1))

print(setify([1,3,6,7,6,3,5])) 

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def mean(num):
    '''This function calculates the mean of all the digits of a number.'''

    count=0
    sum=0
    while(num!=0):
        rem=num%10
        num  =num//10
        count+=1
        sum+=rem

    return sum//count

print("Mean of the digits is : ", mean(666))


