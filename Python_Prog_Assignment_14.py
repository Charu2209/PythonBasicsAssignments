# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

class DivisibleBySeven(object):

    def __init__(self,number):
        self.num=number

    def genfunc(self):
        '''This function iterates over the number between range 0-num ehich are divisible by 7.'''

        for i in range(self.num):
            if i%7==0:
                yield i

obj = DivisibleBySeven(70)
for i in obj.genfunc():
    print(i,end = ' ')

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def computeFreq(str):
    '''This program computes the frequency of the words.'''

    list1 = str.split(' ')
    dict1={}
    for i in list1:
        if i in dict1.keys():
            dict1[i]+=1
        else:
            dict1[i]=1

    # Code for sorting the dictionary
  
    myKeys = list(dict1.keys())
    myKeys.sort()
    sorted_dict = {i: dict1[i] for i in myKeys}

    for k,v in sorted_dict.items():
        print(k,':',v)

computeFreq('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')


# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

class Person:
    def getGender(self):
        pass

class Male(Person):

    def getGender(self):

        return 'Male'

class Female(Person):

    def getGender(self):
        return 'Female'
    
obj=Male()
print(obj.getGender())

obj=Female()
print(obj.getGender())

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def genFunction(subject,verb,object):

    '''This function generates all the sentenses that can be formed using the subject, verb and object lists'''

    for i in subject:
        for j in verb:
            for k in object:
                print(i+' '+j+' '+k+'.')

genFunction(['I','You'], ['Play', 'Love'],['Hockey','Football'])



# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")


import zlib
'''This program compresses or decompresses the data'''
text=b"hello world!hello world!hello world!hello world!"
comp=zlib.compress(text)
print("Compressed: ", comp)
decomp=zlib.decompress(comp)
print("Decompressed: ", decomp)


# Question 6
print("\n")
print("Question 6 Solution")
print(120*"-")


def binary_search(arr, low, high, x):

	if high >= low:

		mid = (high + low) // 2

		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")








 

    

