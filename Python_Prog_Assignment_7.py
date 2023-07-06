# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def sumArray(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

print("Sum of array is : {}".format(sumArray([2,4,5,6])))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def maxArray(arr):
    '''This function finds the maximum number in an array.'''
    if(len(arr))==1:
        print("Maximum is : ",arr[0])
    elif(len(arr)==0):
        print("List is empty")
    else:
        max=arr[0]
        for i in range(1,len(arr)):
            if max<arr[i]:
                max=arr[i]
        print("Maximum is : ",max)

maxArray([1])

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")
        
def arrRotation(arr,n):
    '''This function rotates the n elements of the array'''
    for i in range(0,n):
        el=arr[0]
        arr.remove(el)
        arr.append(el)
    return arr

print("Array after rotation : {} ".format(arrRotation([5,6,7,8,9,0,1],3)))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def split_add_array(arr,n):
    '''This function split array part and add it to the end of the array.\n
    Parameters:\n
    n(int) - number of elements to be add at the end.'''

    print('Array after split and addition {} : '.format(arrRotation(arr,n)))

split_add_array([4,6,7,8,9,0,1,2,3],3)

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def isMonotonic(arr):

    '''This function check whether the given array is monotonic or not? '''
    if(arr[0]>arr[1]):
            for i in range(0,len(arr)-1):
                if(arr[i]<arr[i+1]):
                    return False
    else:
            for i in range(0,len(arr)-1):
                if(arr[i]>arr[i+1]):
                    return False
    return True

print("Is array monotonic : ",isMonotonic([5,4,3,6]))
 