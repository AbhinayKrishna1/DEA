import json
'''
x='{"Name":"xyz","age":35}'
z=json.loads(x)                 #Used to Convert JSON to Dictionary
print(z["Name"])
print(z["age"])
x={"name":"xyz","age":35}
y=json.dumps(x)                 #Used to Convert Dictionary to JSON
print(y)
'''
import re
'''                               #Regular Expression
x="The rain in spain"
y=re.search("^The.*spain$",x)
if y:
    print("Yes")
else:
    print("No")
y=re.findall("ai",x)
print(y)
z=re.search("\s",x)
print(z)
z=re.split("\s",x)
print(z)
'''
'''
t="there are 123 ap 234 234  5 57 6 43 ples"
p=r"\d+"
match=re.search(p,t)
if match:
    print(match)
'''

import logging as l
'''
'''
'''
l.basicConfig(level=l.DEBUG)
l.debug("Hello, Debug!")
l.info("Hello, Info!")
l.warning("Hello, Warning!")
l.error("Hello, Error!")
l.critical("Hello, Critical!")
'''

l.basicConfig(level=l.DEBUG, filename="app.log",filemode="a",format="%(name)s - %(levelname)s - %(message)s")
l.debug("Hello, Debug!")
l.info("Hello, Info!")
l.warning("Hello, Warning!")
l.error("Hello, Error!")
l.critical("Hello, Critical!")
'''
'''
'''
for i in range(11):                #pylint
    print(i)
'''                                 #Exception Handling
'''
try:
    x10/0
except:
    print("Divided by zero")
finally:
    print("Completed Execution")
'''
'''
try:
    n=int(input())
    r=10/n

except ValueError as e:
    print("Invalid input",e)
except ZeroDivisionError as e:
    print("Zero cant be inserted")
except:
    print("Unexpected")

else:
    print("Result",r)
finally:
    print("Completed")
'''
'''
def check(a):
    if a > 18:
        print("Eliglible")
    else:
        raise ValueError("Less than 18 Wait")
try:
    check(12)
except ValueError as e:
    print("Not Eligible")
'''
'''
class NotEligible(Exception):                       #User Defined Exceptions
    print("Exception")
def check(a):
    if a > 18:
        print("Eligible")
    else:
        raise NotEligible("Less than 18")
try:
    check(21)
except NotEligible as e:
    print("Not eligible")
'''
'''
f=open("text.txt","r+")                                 #File Handling
f.write("Welcome to Chenni")
f.write("Elluriki Vannakam")
f.close()
'''
'''
f=open("text.txt","r")
print(f.read())
f.close()
'''
'''
f=open("text.txt","a")
f.write("Hi Hello")
f.write("Good Morning")
f.close()
'''

import os                             #to Cheack whether the file exists or not
'''
if os.path.exists("txt.txt"):
    with open("txt.txt","r") as file:
              c=file.read()
              print(c)
else:
    print("file does not exist")
'''
'''
try:
    with open("text1.txt","r") as file:
        d=file.read()
    with open("text1.txt","w") as filewrite:
        filewrite.write(d)
    print("File copied successfully")
except FileNotFoundError:
    print("Input or output Operation file")
except IOError as e:
    print("I/O Exception",e)
except Exception as e:
    print("Unexpected Error")
'''
'''
os.remove("text.txt")                       #Deletes a  File
'''
'''
f=open("text.txt","x")                       #Creates New File
'''    
import mysql.connector
myDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
print(myDB)





































