#Password Check
'''
s=input()
import re
if len(s)>=8:
    p=r".[A-Z]"
    m=re.findall(p,s)
    pp=r".[a-z]"
    n=re.findall(pp,s)
    ppp=r".\d+"
    o=re.findall(ppp,s)
    print(m)
    print(n)
    print(o)
    if m and n and o:
        print("Great Password")
    else:
        print("Not Strong Pass")
        
else:
    print("Please Enter Another Password")

'''
'''
s=input()                        #URL Checker
import re
p=r"^(http|https)://www.+(com|in)/$"
m=re.findall(p,s)
print(m)
if m:
    print("Match")
else:
    print("Not")

'''
'''
try:                            #ValueError
    s=int(input())
except ValueError as e:
    print("Error! Raised!,, Enter correct Integer Value")
'''
'''
try:                            #TypeError
    s=input()
    t=s+10
except TypeError as e:
    print("Error! Raised!,, Enter correct String Value")
 '''
'''
try:                            #ZeroDivisionError
    k=int(input())
    s=10/k
except ZeroDivisionError as e:
    print("Zero cannot be given")
else:
    print(s)
'''
'''    
try:
    if True:
        a=  7
            print a
except SyntaxWarning as e:
    print("Check Indentation")
'''









