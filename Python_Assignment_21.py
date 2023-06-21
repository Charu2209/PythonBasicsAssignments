# Question 1
print('\n')
print("Question 1 Solution")
print(120*"-")

from datetime import date

file = open('today.txt','w')
file.write(str(date.today()))
file.close()

print("See the file today.txt for current date")

# Question 2
print('\n')
print("Question 2 Solution")
print(120*"-")

file = open('today.txt','r')
today_string=file.readline()
print(today_string)
file.close()

# Question 3
print('\n')
print("Question 3 Solution")
print(120*"-")

file = open('today.txt','r')
today_string=file.readline()
print(today_string)
file.close()

# Question 4
print('\n')
print("Question 4 Solution")
print(120*"-")

import os

print("List of files in current directory:")
for i in os.listdir():
    print(i)

# Question 5
print('\n')
print("Question 5 Solution")
print(120*"-")

print("List of files in parent directory:")
for i in os.listdir('../'):
    print(i)


# Question 6
print('\n')
print("Question 6 Solution")
print(120*"-")

import multiprocessing,time,datetime
def process1():
    
    time.sleep(4)
    print("Process1",datetime.datetime.now())

def process2():
    
    time.sleep(1)
    print("Process2",datetime.datetime.now())

def process3():
    
    time.sleep(2)
    print("Process3",datetime.datetime.now())

start = time.time()

print(datetime.datetime.now())
if __name__=="__main__":



    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)
    p3 = multiprocessing.Process(target=process3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

end = time.time()


print("It takes " +str(end-start)+" seconds")

# Question 7
print('\n')
print("Question 7 Solution")
print(120*"-")

x = datetime.datetime(1996, 5, 17)

print(x)

# Question 8
print('\n')
print("Question 8 Solution")
print(120*"-")

print('day Name:', x.strftime('%A'))

# Question 9
print('\n')
print("Question 9 Solution")
print(120*"-")

from datetime import timedelta

print(x + timedelta(days=10000))



