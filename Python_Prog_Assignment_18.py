# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def filter_list(l):
    '''This function returns the list after removing all the string elements.'''

    return [i for i in l if type(i)==int]

print("Modified List : ",filter_list([1,2,'a','b']))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def reverse(s):
    '''The "Reverse" takes a string as input and returns that string in reverse order, with the 
        opposite case.'''
    
    result=''
    
    for i in s:

        if ord(i)==32:
            result+=i
        elif ord(i) in range(97,123):
            #character is in lowercase
            result+=i.upper()
        elif ord(i) in range(65,91):
            result+=i.lower()
    return result[::-1]

print('Result : ', reverse('Hello World'))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

list1=[1,2,3,4,5,6,7,8,9,0]
first,middle,last=list1[0],list1[1:-1],list1[-1]
print("first -->",first,"\n","middle -->",middle,'\n',"last -->",last)

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def factRecursion(num):
    '''This function calculates the factorial of number recursively.'''

    if num==0:
        return 1
    else:
        return num*factRecursion(num-1)

print(factRecursion(4))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def move_to_end(list1,num):
    '''This function moves all the num to the end of the list'''
    [list1.append(list1.pop(i)) for i in range(len(list1)) if list1[i]==num]

    print(list1)

move_to_end([7,8,9,1,2,3,4],9)

