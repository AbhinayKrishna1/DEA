'''
b=lambda a: a**2 #Lambda Function
print(b(3))

u=lambda a: a.upper()
print(u("abhinay"))
'''
'''
a= lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zeo" #Ternary Experssion
print(a(5))

x=10
y=20
a= x+y if x>y else x-y
print(a)
'''
'''
l=[lambda arg=x : arg*10 for x in range(1,5)] #List Comperehension using lambda function
for i in l:
    print(i())
'''
'''
c=lambda x: "Odd" if x%2!=0 else "Even"
print(c(5))
'''
'''
c= lambda x,y: [x+y,x-y] #Lambda with Multiple Statements
r=c(1,2)
print(r)
'''
'''
n=[2,23,4,45,5,3,4,5,4] #Filter Method Using Lambda function
e=filter(lambda x:x%2==0,n)
print(list(e))
'''
'''
a=[1,2,3,34,4,324,2,34,2,2] #Map
b=(lambda x: x*2,a)
print(list(b))
'''
'''
from functools import reduce #Reduce
a=[1,3,2,346,3,2,45,3,3]
b=reduce(lambda x,y:x*y,a)
print(b)
'''
'''
a="Abhinay"
b=22
m="My name is {} and I am {} years old".format(a,b)
print(m)
print("My name is {} and I am {} years old".format(a,b))

c=f"Hi {a}, are you {b} years old?"
print(c)
print(f"Hi ! {a} and Your age is {b} right")
'''
'''
def a(m): #Inner Funcions
    def b():
        print(m)
    b()
a("hi")
'''

'''
def decorator(aa): #Decorator
    def wrapper():
        print("Decorator Welcomes You")
        aa()
    return wrapper
@decorator
def a():
    print("Hi")
a()

import inspect #Function Signatures
print(inspect.signature(a))

'''
'''
class Dog:
    sound="Bark"
d=Dog()
print(d.sound)
'''
'''
class Dog: #Class
    species="Canine"
    def __init__(self,name,age): #Constructor
        self.name=name
        self.age=age
    def __str__(self): #It is used to print the bject ie like toString()
        return f"{self.name} is {self.age} years old."
d=Dog("german Shepard",22)
print(d.name)
print(d)
print(d.species)
'''
'''
class Dog: #Class
    species="Canine"
    def __init__(self,name,age): #Constructor
        self.name=name
        self.age=age
    def __str__(self): #It is used to print the bject ie like toString()
        return f"{self.name} is {self.age} years old."
d=Dog("german Shepard",22)
print(d.name)
d.name="Bull Dog"       #Modifiying using object
print(d.name)
print(d)
d.species="Narrow"
print(d.species)
d1=Dog("Lab",12)
print(d1.name)
print(d1.species)
'''
'''
class Details:      #Inheritance
    def __init__(self,name,age,roll,city):
        self.name=name
        self.age=age
        self.roll=roll
        self.city=city
    def details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll:",self.roll)
        print("City:",self.city)
class Student(Details):
    def details(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Age:",self.age)
        print("City:",self.city)
        
d=Details("abhinay",21,21,"Narasaraopet")
s=Student("Midhun",22,22,"Guntur")
s.details()
d.details()
d.name="Krishna"
d.details()
'''
'''
class Car:
    def __init__(self):
        self.name="Model"
        self.tt=self.tata()
    def show(self):
        print("Name:",self.name)
    class tata:
        def __init__(self):
            self.name="Harrier"
            self.model="SUV"
        def display(self):
            print("Name:",self.name)
            print("Model:",self.model)
c=Car()
tt=tata()
tt.display()
'''
'''
class parent:            #Super Keyword
    def show(self):
        print("Iam Parent")
class child(parent):
    def show(self):
        print("Iam Child")
        super().show()
c=child()
c.show()
'''
'''
class pri:              #Private
    def __init__(self):
        self.__salary=50000
    def s(self):
        print(self.salary)
p=pri()
#print(p.salary)
p.s()
'''
'''
n=[1,2,3,4,5,5,6]         #iter and next,,, They are used to iterate a iterable sequentially
i=iter(n)
print(next(i))
print(next(i))
'''
'''
def m():                  #Local Scope
    x=30
    print(x)
m()
'''
'''
def m():                #Enclosing Scope
    x=300
    def n():
        print(x)
    n()
m()
'''
'''
global x                   #Global Scope
x=30

def m():
    print(x)
print(x)
m()
'''
'''
import pytask1              #Module Example
pytask1.p()
pytask1.prime()
'''
'''
import math                 #Math Module
print(min(1,2))
print(abs(-122213))
print(max(5,43))
'''
import numpy as np            #Numpy
'''
arr=np.array([1,2,3,4,5,45,43])
print(arr)
print(type(arr))
print(np.zeros((2,3)))
print(np.ones((3,2)))
print(np.arange(0,10))
print(np.linspace(0,1,5))
print(np.random.rand(1,5))
a=np.array([1,34,2])            #Array Operations
b=np.array([4,5,32])
print(a+b)
print(a-b)
print(a*b)
print(a**2)
print(np.sqrt(b))
print(np.sqrt(a))
c=np.array([[1,2],[3,4]])       #Matrix Operations
d=np.array([[5,6],[6,7]])
print(np.dot(c,d))
print(np.transpose(c))
print(np.linalg.inv(c))
print(c[0,1])                   #Slicing in Arrays 
print(c[:,1])
print(c[1])
e=np.array([1,3,2,2,3,5,6])     #Array static operations     
print(e.mean())
print(e.max())
print(e.min())
print(e.sum())
print(e.std())
'''
import pandas as pd              #Pandas
'''
s=pd.Series([10,20,30,40],index=["a","b","c","d"])      #Series in pandas
print(s)
d={"Name":["abhinay","Midhun","Venkata","Krishna"],"age":[21,22,23,24],"city":["NRT","VIJ","HYD","CHENNAI"]}
df=pd.DataFrame(d)                                      #DataFrames in Pandas            
print(df)


print(df.describe())
print(df.head())
print(df.tail())
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.shape)
print(df.columns)
print(df["age"])
print(df[["age","city"]])
print(df[df["age"]>22])
df["Country"]="INDIA"
print(df)
df.rename(columns={"age":"years"},inplace=True)
print(df)
df["years"]+=1
print(df["years"])

'''








