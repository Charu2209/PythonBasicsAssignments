# Question 1
print("Question 1 Solution")
print(120*"-")

test1='This is a test of the emergency text system'

#Saving to file

text_file = open("text.txt",'w')
text_file.write(test1)
text_file.close()
print("See the test.txt file for the solution")

# Question 2
print('\n')
print("Question 2 Solution")
print(120*"-")


#Reading content of file

file = open('text.txt','r')
test2 = file.readline()
file.close()

print(test2)

# Question 3
print('\n')
print("Question 3 Solution")
print(120*"-")

import csv 

row_list=[['title','author','year'],['The Weirdstone of Brisingamen','Alan Garner',1960],['The Weirdstone of Brisingamen','Alan Garner',1960],
          ['Thud!','Terry Pratchett',2005],['The Spellman Files','Lisa Lutz',2007],['Small Gods','Terry Pratchett',1992]]

with open('books.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(row_list)

file.close()
print("See books.csv for the solution")


# Question 4
print('\n')
print("Question 4 Solution")
print(120*"-")

import sqlite3

#creating database
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# creating table

cur.execute("CREATE TABLE IF NOT EXISTS books ([title] TEXT, [author] TEXT,[year] INTEGER)")

conn.commit()
conn.close()

print("Books.db database has been created in your current directory")

# Question 5
print('\n')
print("Question 5 Solution")
print(120*"-")

with open('books.csv','r') as file:
    file_reader = csv.reader(file,delimiter=',')

    #skip the csv header
    next(file_reader,None)

    # create fileds 
    title =''
    author=''
    year=''

    # creating database connection
    conn=sqlite3.connect('books.db')
    c= conn.cursor()

    # putting csv data
    for row in file_reader:
         #skip the first row
         for i in range(len(row)):
              title = row[0]
              author = row[1]
              year = row[2]
         #Create Insert Query
         InsertQuery = f"INSERT INTO books Values ('{title}','{author}','{year}')"

         c.execute(InsertQuery)

print("CSV data has been inserted")
# Commit Changes
conn.commit()
conn.close()

# Question 6
print('\n')
print("Question 6 Solution")
print(120*"-")

conn = sqlite3.connect('books.db')
c=conn.cursor()

# Reading Data
c.execute("Select title from books order by title desc")
rows=c.fetchall()

for i in rows:
     print(i)


conn.close()

# Question 7
print('\n')
print("Question 7 Solution")
print(120*"-")

conn = sqlite3.connect('books.db')
c=conn.cursor()

# Reading Data
c.execute("Select * from books order by year asc")
rows=c.fetchall()

for i in rows:
     print(i)

conn.close()

# Question 8
print('\n')
print("Question 8 Solution")
print(120*"-")


# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///books.db')

print("connection has been estabilished")

# Question 9
print('\n')
print("Question 9 Solution")
print(120*"-")


import redis
conn = redis.Redis()
conn.delete('test')
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hgetall('test')
     
# Question 10
print('\n')
print("Question 10 Solution")
print(120*"-")

conn.hincrby('test','count', 3)
     


