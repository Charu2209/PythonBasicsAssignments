# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def uniqueDictValues(dict1):
    '''This program extracts the unique dictionary values'''

    set1 = set(dict1.values())
    return set1

print("Unique Dictionary values are {}".format(uniqueDictValues({'a':'1234','b':'234','c':'45','d':'45'})))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def sumItemDict(dict1):
    '''This program  do sum of all items in dictionary.'''

    list1=dict1.values()
    sum=0
    
    for i in list1:
        sum+=int(i)

    return sum

print("Sum of dictionary values is : {}".format(sumItemDict({'a':'1234','b':'234','c':'45','d':'45'})))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def mergeDict(dict1,dict2):

    '''This function merges the 2 dictionary.'''

    result = {**dict1,**dict2}
    return result

print("Dictinary after merging : {}".format(mergeDict({'a':'123','b':'34'},{'c':'56','d':'7'})))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

from itertools import product
def list_to_dict(dict1):
    '''Key value list to flat dictionary.'''

    keys = list(dict1.keys())
    result = dict(zip(dict1[keys[0]], dict1[keys[1]]))
    return result

print("Flatten Dictionary : {}".format(list_to_dict({'a':[1,2,3],'b':['ab','bc','cd']})))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def insertionFront(key,value,dict1):
    '''This function add key value to front of the dictionary.'''
    temp={}
    temp[key]=value
    result ={**temp,**dict1}
    return  result

print("Dictionary affter adding elements to the front : {} ".format(insertionFront('a',123,{'d':34,'e':109})))

# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")

from collections import OrderedDict
def check_order(my_input, my_pattern):
    my_dict = OrderedDict.fromkeys(my_input)
    pattern_length = 0
    for key,value in my_dict.items():
        if (key == my_pattern[pattern_length]):
            pattern_length = pattern_length + 1
        if (pattern_length == (len(my_pattern))):
            return True
    return False

print("Order is correct : {} ".format(check_order("engineers rock",'re')))

# Question 7
print("\n")
print("Question 7 Solution")
print(120*"-")

def sortDict(dict1):
    keys = list(dict1.keys())
    keys.sort()
    return {key:dict1[key] for key in keys}

print("Sorted Dictionary is : {}".format(sortDict({'a':'123','d':'45','c':'09','b':'965'})))


    


