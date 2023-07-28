# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def double_char(s):
    '''This function repeats each character of the string.'''

    result=''

    for i in s:
        result+=i+i

    print(result)

double_char("Hello World")

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def reverse(bool1):
    '''This function reverse the boolean input'''

    if type(bool1)==bool:
        return not bool1
    else:
        return "boolean expected"

print(reverse(None))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def num_layers(layer):
    '''This function returns the thickness of the paper after folding it into input no of times.'''

    print( 0.5*2**layer*0.001)

num_layers(1)

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def index_of_caps(s):
    '''This function that takes a single string as argument and returns an ordered list containing
the indices of all capital letters in the string.'''

    return [s.index(i) for i in s if ord(i) in range(65,91)]

print(index_of_caps('eDaBiT'))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def find_even_nums(num):
    '''This function finds all even numbers from 1 to the given number.'''

    return [i for i in range(1,num+1) if i%2==0]

print(find_even_nums(8))





    

