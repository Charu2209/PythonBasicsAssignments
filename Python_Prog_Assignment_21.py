# Question 1
print("\n")
print("Question 1 Solution")
print(120*"-")

def next_in_line(l,num):
    '''This function that takes a list and a number as arguments. Add the number to the end of
        the list, then remove the first element of the list.'''
    
    l.append(num)
    l.pop(0)
    return l

print(next_in_line([5,6, 7, 8, 9], 1))

# Question 2
print("\n")
print("Question 2 Solution")
print(120*"-")
      
def get_budgets(list_dict):
    '''This function takes a list of dictionaries and returns the sum of people's budgets.'''

    sum=0
    for i in list_dict:
        sum+=i['budget']
        
    return sum

print(get_budgets([
            { 'name': 'John', 'age': 21, 'budget': 23000 },
            { 'name': 'Steve', 'age': 32, 'budget': 40000},
            { 'name': 'Martin', 'age': 16, 'budget': 2700 }]))

# Question 3
print("\n")
print("Question 3 Solution")
print(120*"-")

def alphabet_soup(s):
    '''This function takes a string and returns a string with its letters in alphabetical order.'''

    temp=[i for i in s]
    temp.sort()
    return ''.join(temp)
print(alphabet_soup("hello"))

# Question 4
print("\n")
print("Question 4 Solution")
print(120*"-")

def compund_interest(p,t,r,total_compunding_period):
    '''This function calculaes the compund interest.'''

    a= p*pow((1+(r/total_compunding_period)),total_compunding_period*t)
    return round(a,2)

print(compund_interest(10000, 10, 0.06, 12))


# Question 5
print("\n")
print("Question 5 Solution")
print(120*"-")

def filter_list(l):
    ''' The function takes a list  and filters out the list so that it returns a list of integers only.'''

    return [i for i in l if type(i)==int]
print(filter_list([1,2,3,'a','b',True]))




    