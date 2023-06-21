print("Question 1 Solution")
# Qustion 1

class things():
    pass
print(things())

example = things()
print(example)

## Yes, Both the printed values are same

print("\n")
print(120*"-")
print("Question 2 Solution")

# Question 2
class Thing2():
        
    letters = 'abc'
    
print(Thing2.letters)

print("\n")
print(120*"-")
print("Question 3 Solution")

# Question 3

class Thing3():
    
    def __init__(self):
        self.letters = 'xyz'

obj=Thing3()
print(obj.letters)

#Ans - yes, we need to make the object to print the letters value

print("\n")
print(120*"-")
print("Question 4 Solution")

# Question 4

class Element():

    def __init__(self,name,symbol,number):

        self.name=name
        self.symbol=symbol
        self.number=number

obj=Element('Hydrogen','H',1)
print("name : ", obj.name, " | symbol : ", obj.symbol, " | number : ",obj.number)

print("\n")
print(120*"-")
print("Question 5 Solution")

# Question 5
dict = {'name' : 'Hydrogen','symbol':'H','number' : 1}
obj = Element(dict['name'],dict['symbol'],dict["number"])
print("name : ", obj.name, " | symbol : ", obj.symbol, " | number : ",obj.number)

print("\n")
print(120*"-")
print("Question 6 Solution")

# Question 6

class Element():

    def __init__(self,name,symbol,number):

        self.name=name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print("name : ", self.name, " | symbol : ", self.symbol, " | number : ",self.number)


hydrogen=Element('Hydrogen','H',1)
hydrogen.dump()

print("\n")
print(120*"-")
print("Question 7 Solution")

#Question 7

print(hydrogen)

class Element():

    def __init__(self,name,symbol,number):

        self.name=name
        self.symbol=symbol
        self.number=number

    def __str__(self):
        print("name : ", self.name, " | symbol : ", self.symbol, " | number : ",self.number)


print(hydrogen)
# No change in values

# Question 8

print("\n")
print(120*"-")
print("Question 8 Solution")

class Element():

    def __init__(self,name,symbol,number):

        self._name=name
        self._symbol=symbol
        self._number=number

    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol
    
    def get_number(self):
        return self._number


hydrogen=Element('Hydrogen','H',1)
print(hydrogen.get_name())
print(hydrogen.get_symbol())
print(hydrogen.get_number())


# Question 9
print("\n")
print(120*"-")
print("Question 9 Solution")

class Bear():

    def eats(self):
        print('berries')

class Rabbit():
    def eats(self):
        print('clover')

class Octothorpe():
    def eats(self):
        print('campers')

bear_obj = Bear()
rabbit_obj = Rabbit()
Octothorpe_obj = Octothorpe()

bear_obj.eats()
rabbit_obj.eats()
Octothorpe_obj.eats()

# Question 10

print("\n")
print(120*"-")
print("Question 10 Solution")

class Laser():
    def does(self):
        print('disintegrate')

class Claw():
    def does(self):
        print('crush')

class SmartPhone():
    def does(self):
        print('ring')

class Robot(Laser,Claw,SmartPhone):

    def __init__(self):
        self.laser_obj = Laser()
        self.claw_obj = Claw()
        self.phone_obj = SmartPhone()

    def does(self):
        self.laser_obj.does()
        self.claw_obj.does()
        self.phone_obj.does()

robot_obj = Robot()
robot_obj.does()






    