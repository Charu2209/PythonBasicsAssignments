# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")


def genfunc():
    '''This function iterates over the number between range 0-num and prints the numbers
     that are divisible by 5 and 7.'''
    num = int (input("Enter the number : "))

    for i in range(num):
        if i%7==0 and i%5==0:
              yield i

for i in genfunc():
     print(i, end= ' ')

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def genfunc():
    '''This function iterates over the number between range 0-num and prints the even numbers.'''
    num = int (input("Enter the number : "))

    for i in range(num+1):
        if i%2==0:
              yield i

for i in genfunc():
     print(i, end= ',')

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def fiboListComp():
    '''This function prints the fibbonacci series using list comprehension'''

    num = int(input("Enter the number : "))
    series=[0,1,1]
    [series.append(series[k-2]+series[k-1]) for k in range(3,num+1)]
    print(series)

fiboListComp()

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def username(email):
    '''This function prints the username only from the input.\n
    Input : username@companyname.com\n'''

    print("Username is : ",email.split('@')[0])

username("john@google.com")

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

class Shape:
    
    def area():
        print(0)

class Square(Shape):
    
    def __init__(self,length=0):
        Shape.__init__(self)
        self.length=length

    def area(self):
         print( self.length*self.length)

obj = Square()
obj.area()

