# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def equal(a,b,c):
    '''This program prints the amount of integers that are equal.'''

    if a==b and a==c:
        return 3
    elif a==b or a==c or b==c:
        return 2
    else:
        return 0
    
print(equal(3, 4, 1))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def dict_to_list(dict1):
    '''This function converts a dictionary items into list of key value tuples.'''

    list1= [(k,v) for k,v in dict1.items()]
    list1.sort(key=lambda x:x[0])
    return list1

print(dict_to_list({
'D': 1,
'B': 2,
'C': 3
}))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def mapping(list1):
    '''This function creates a dictionary with each (key, value) pair being the (lower case,
    upper case) versions of a letter, respectively.'''

    dict2={}
    for i in list1:
        dict2[i]=i.upper()

    return dict2

print("New dictionary : ",mapping(['p', 's']))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def vow_replace(s,vow):
    '''This function replaces all the vowels within the string with the specified vowel.'''

    result = [i if i not in ['a','e','i','o','u'] else vow for i in s]
    return ''.join(result)

print(vow_replace('apples and bananas', 'u'))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def ascii_capitalize(s):
    '''This function capitalizes the character if its ascii code is even else lowers the character.'''

    result=''

    for i in s:
        if ord(i)%2==0 and ord(i)!=32:
            result+=i.upper()
        elif ord(i)==32:
            result+=i
        else:
            result+=i.lower()

    return result

print(ascii_capitalize('to be or not to be'))






     
