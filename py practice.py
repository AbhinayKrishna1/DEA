"""fs=frozenset({1,2,3})
print(fs)
"""
"""
b=bytes([65,66,67])
print(b)
"""
'''
x=None
print(type(x))
'''
'''
y
print(y)
'''
'''
a=int(input()) #Elif
b=int(input())
if a>b:
    print(a,"is greater than",b)
elif a<b:
    print(a,"is less than",b)
else:
    print(a,"is equal to",b)
'''
'''
a=int(input()) #Nested If-Else
if a!=0:
    if a>0:
        print(a,"is positive")
    else:
        print(a,"is negative")
else:
    print(a,"is zero")
'''
'''
n=10 #While LOOP
while n>0:
    print(n)
    n=n-1
'''
'''
n=5
while n > 0: #Break
    if n==3:
        break
    print(n)
    n=n-1
'''
'''
b=(1,2,2,3) #Iterating over a object
for i in b:
    print(i)
'''
'''
a=[1,2]
b=[3,4]
for i in a: #Nested For loop
    for j in b:
        print(i,j)

'''
'''
def greet(): #Function
    print("Hi Hello Mate!")
greet()
'''
'''
n=input() #Function Parameters
def greet(n):
    print("Hi Hello Mate",n,"!")
greet(n)

'''
'''
def add(a,b): #Returning a Function
    return a+b
r=add(1,3)
print(r)
'''
'''
def greet(a="guest"): #Default Parameter
    print("Hi!",a)
greet("Abhinay")
'''
'''
def inn(): #Returning Multiple Values
    name="abb"
    age=21
    return age,name
a,b=inn()
l=inn()
print(l,a,b,sep="\n")
'''
'''
def add(*n): #Variable Number of Arguements
    return sum(n)
print(add(1,23,3,4,234,5,3,4,5,35,364,436))
'''
'''
def a(**args): #Keyword Arguements
    for i in args:
        print(args[i])
a(n="abhi",age=21,ph=2324323)

'''
'''
from array import array
f=array('u',"applebanna")#Array
print(f)
for i in f:
    print(i)

numbers=array('i',[1,2,6,454,86,3,4,5])
length=len(numbers)
print(length)
numsorted=sorted(numbers)
print(numsorted)
'''
