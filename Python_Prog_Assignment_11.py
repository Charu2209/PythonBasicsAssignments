# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

import functools

def wordsGreaterLength(st,k):
    '''This functions finds all the words greater than length k in the given string'''
    l = st.split(' ')
    return [a for a in l if len(a)>k]

print("Words having length greater than k are : {}".format(wordsGreaterLength('My name is shantanu.',3)))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def removeithFromString(st,i):
    '''This function removes ith character from the string'''

    return ''.join([a for a in st if st[i-1]!=a])

print("String after removing ith element : {}".format(removeithFromString('abcde',3)))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def splitString(s,key):
    '''This function split the string based on the character provided.'''

    l=[]
    if key != '':
        for i in s:
            if s!=key:
                l.append(s)
        return l
    elif key == '':
        return [a for a in s]

print("Result after split : {}".format(splitString('abcde','')))

def joinString(s,key):
    "This function joins the string based on the key provided."

    result=''
    for i in s:
        result = result+i+key

    return result[:-1]
print("Result after join : {}".format(joinString(['a','b','c','d','e'],'-')))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def isBinary(s):
    '''This program checks if the given string is binary or not.'''

    set1 = set(s)
    for i in s:
        if i!='0' and i!='1':
            return False
    return True

print('Given string is Binary : ',isBinary('0100011s'))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def uncommonWords(str1,str2):
    '''This function finds uncommon words from 2 strings.'''
    result=[]
    set1 = set(str1.split(' '))
    set2 = set(str2.split(' '))

    result = [elements for elements in set1 if elements not in set2]
    result2 =[elements for elements in set2 if elements not in set1]


    return result+result2

print('List of uncommon words are : {}'.format(uncommonWords('I am a girl', 'I am a boy.')))

# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")

def duplicateChar(s):
    '''This function prints all duplicate character in string'''

    result = [char for char in s if char in s[s.find(char)+1:]]
    return set(result)

print('Duplicates characters are: {}'.format(duplicateChar('aabccdeefgh')))

# Question 7
print("\n")
print("Question 7 Solution")
print(120*"-")

def anySpecialChar(s):
    specialChar = "&*{}[],=-().+;'/ "

    if([i for i in specialChar if i in s]):
        return True
    return False

print('Is string contain any special characters : ', anySpecialChar('abcde'))












