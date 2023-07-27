# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def sumEvenlyDivide(a,b,c):
    '''This function prints the sum of the numbers which are evenly divisible by c within the range a,b'''

    sum=0
    for i in range(a,b+1):
        if i%c==0:
            sum+=i
        
    return sum

print("sum of evenly divided numbers is : ", sumEvenlyDivide(1,10,2))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def checkInequality(exp):

    '''This function evaluates the inequality function.'''

    if(eval(exp)):
        return True
    return False

print("Given inequality function is true : ", checkInequality("2<7>15"))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def replaceVowelWithChar(s,charac):

    '''This function replaces all the vowel in the string with specified character.'''

    for i in s:
        if ord(i) in [97, 101, 105, 111, 117, 65, 69, 73, 79, 85]:
            s=s.replace(i,charac)   
    print("Modified string is : ",s)

replaceVowelWithChar("minnie mouse","?")

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

def hammingDist(str1,str2):
    '''This function calculates the hamming distance between the 2 strings.
    '''
    dist = abs(len(str1)-len(str2))
    
    if len(str1)<len(str2):
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                dist+=1

    else:
        for i in range(len(str2)):
            if str1[i]!=str2[i]:
                dist+=1

    return dist
print(hammingDist('abcde',"abcf"))


            
