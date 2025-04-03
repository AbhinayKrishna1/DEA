#TASKS

#List Functions
'''
a=[]
a.append(2)
print(a)
a.extend([2,3,3,3])
print(a)
a.append([23,1,2])
print(a)
a.remove(2)
print(a)
a.pop()
print(a)
a.insert(0,1)
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
del a
print(a)
'''

#String Functions
'''
a="abhinaykrishna"
print(a.capitalize())
print(a.casefold())
print(a.title())
print(a.count("a"))
print(a.endswith("s"))
print(a.startswith("A"))
print(a.index("b"))
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.isalpha())
print(a.isalnum())
print(a.isdigit())
print(a.isdecimal())
print(a.rfind("h"))
print(a.find("h"))
print(a.strip())
print(a.rstrip())
print(a.split())

print(len(a))
'''
#Tuple Functions
'''
a=(1,34,2,4,2,5,1,4,4,3,5,2)
print(a.count(1))
print(a.index(4))
print(len(a))
print(a[::-1])
'''

#Grading Task
'''
n=int(input())
if n>40:
    if n>=80 and n<=100:
        print("Grade is A")
    elif n>=70 and n<80:
        print("Grade is B")
    elif n>=60 and n<70:
        print("Grade is C")
    elif n>=50 and n<60:
        print("Grade is D")
else:
    print("Grade is F")
'''    



#Reverse a string
'''
a=input()
print(a[::-1])
'''
#check for palindrome
'''
a=input()
if a==a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#check for prime number
'''
n=int(input())
c=0
for i in range(2,n+1):
    if n%i==0:
        c=c+1
if c==1:
    print("Prime Number")
else:
    print("Not Prime Number")
'''    
    

#fibanocci series
'''
n=int(input())
a=0
b=1
while n>0:
    print(a)
    c=a+b
    b=a
    a=c
    n=n-1
'''
#even or odd
'''
n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
    
'''
#@ for Even,Number for Odd
'''
for i in range(101):
    if i%2==0:
        print("@")
    else:
        print(i)
'''
#Create 2 functions input user details and another functionn is display the values from the user
'''
def inp():
    n=input()
    age=int(input())
    ph=int(input())
    out(n,age,ph)
def out(n,age,ph):
    print(n,age,ph,sep="\n")
inp()
'''
#iterating collection and squaring the iterator
'''
a=[1,2,3,4,1234,54,52,5,2,4,5,6,5,77,6]
for i in a:
    print(i**2)

'''
#Getting Values using Keys in Dictionary
'''
a={"a":21,"b":32,"c":33,"d":3443}
for i in a.keys():
    print(a[i])
'''
#Calculator
'''
a=int(input("Enter Number 1"))
b=int(input("Enter Number 2:"))
c=input("Enter Operation to DO")
if c=="+":
    print(a+b)
if c=="-":
    print(a-b)
if c=="*":
    print(a*b)
if c=="/":
    print(a/b)
'''
