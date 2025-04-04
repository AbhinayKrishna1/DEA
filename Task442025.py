#Types of Inheritance
#Single Inheritance
'''
class a:
    def w(self):
        print("Im A")
class b(a):
    def x(self):
        print("Im B")
B=b()
B.x()
B.w()
'''
#MutliLevel Inheritance
'''
class a:
    def aa(self):
        print("Im Grand Father")
class b(a):
    def bb(self):
        print("Im Father")
class c(b):
    def cc(self):
        print("Im Child")
ccc=c()
ccc.cc()
ccc.bb()
ccc.aa()
bbb=b()
bbb.bb()
bbb.aa()
aaa=a()
aaa.aa()
'''
#Multiple Inheritance
'''
class Father:
    def f(self):
        print("Im father")
class Mother:
    def m(self):
        print("Im mother")
class child(Father,Mother):
    def c(self):
        print("Im child")
cc=child()
cc.c()
cc.f()
cc.m()
'''
#Hierarical Inheritance
'''
class Parent:
    def p(self):
        print("Im Parent")
class child1(Parent):
    def c1(self):
        print("im Child 1")
class child2(Parent):
    def c2(self):
        print("Im Child 2")
cc2=child2()
cc1=child1()
pp=Parent()
cc1.c1()
cc2.c2()
cc1.p()
cc2.p()
pp.p()
'''
#Hybrid Inheritance
'''
class a:
    def aa(self):
        print("Im a")
class b(a):
    def bb(self):
        print("Im b")
class c(b):
    def cc(self):
        print("im c")
class d(c):
    def dd(self):
        print("Im d")
class e(c):
    def ee(self):
        print("Im e")
eee=e()
ddd=d()
ccc=c()
bbb=b()
aaa=a()
eee.aa()
eee.bb()
eee.cc()
eee.ee()
ddd.aa()
ddd.bb()
ddd.cc()
ddd.dd()
ccc.cc()
ccc.bb()
ccc.aa()
bbb.bb()
bbb.aa()
aaa.aa()
'''


#Encapsulation
#Public
'''
class a:
    aa="Hi"
    def show(self):
        print(self.aa)
aw=a()
aw.show()
'''
#Private
'''
class a:
    __aa="Hi"
    print(__aa)
    def show(self):
        print(self.__aa)

class b(a):
    pass
bw=b()
bw.show()
aw=a()
aw.show()
'''
#Protected
'''
class a:
    _aa="Hi"
    print(_aa)
    def show(self):
        print(self._aa)
aw=a()
aw.show()
'''
#Polymorphism
#Overloading
'''#Overloading does not work in python
class a:
    def show(self *a):
        print("Hi")
    def show(self,n):
        print("Good Morning",n)
aa=a()
aa.show()
aa.show("Abbhinay")
'''
#overridding
'''
class a:
    def details(self):
        print("Hi im a")
class b(a):
    def details(self):
        print("Hi im b")
bb=b()
bb.details()
'''

a=[lambda a=i: a*i for i in range(1,20)]
    
print(a())
