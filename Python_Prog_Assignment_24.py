# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def amplify(num):
    '''This function amplifies the number based on certain conditions.'''

    return [i*10 if i%4==0 else i for i in range(1,num+1)]

print(amplify(4))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")

def unique(list1):
    '''This function returns the unique number from the list.'''

    set1=set(list1)
    temp=list(set1)

    for i in temp:
        list1.remove(i)
        if i in list1:
            return temp[1]
        else:
            i
print("Unique number is : ",unique([0, 0, 0.77, 0, 0]))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

class Circle():
    def __init__(self,radius):
        self.radius=radius
    
    def getArea(self):
        return 3.14159265359*self.radius*self.radius
    
    def getPerimeter(self):
        return 2*3.14*self.radius
    
circy=Circle(11)
print("Area of the circle is : ",circy.getArea())

circy=Circle(4.44)
print("Perimeter of the circle is : ",circy.getPerimeter())

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def sort_by_length(list1):
    '''This function sorts the list of string by length.'''

    return sorted(list1,key=len)

print("Sorted list is : ", sort_by_length(['Google', 'Apple', 'Microsoft']))

# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def is_triplet(a,b,c):
    '''This function checks whether the given numbers are pythagorean triplet.'''

    max1=max([a,b,c])

    if a==max1:
        if a**2==b**2+c**2:
            return True
    elif b==max1:
        if b**2==a**2+c**2:
            return True
    else:
        if c**2==b**2+a**2:
            return True
    return False

print("Is pythagorean triplet : ",is_triplet(1, 2, 3))
        



