# Single Inheritance...

# class A:
#     def getA(self,a):
#         self.a=a
#     def putA(self):
#         print("A : ",self.a)

# class B(A):
#     def getB(self,b):
#         self.b=b
#     def putB(self):
#         print("B : ",self.b)

# b1=B()
# b1.getA(10)
# b1.getB(20)
# b1.putA()
# b1.putB()

#  Multi-Level Inheritance..

# class A:
#     def getA(self,a):
#         self.a=a
#     def putA(self):
#         print("A : ",self.a)

# class B(A):
#     def getB(self,b):
#         self.b=b
#     def putB(self):
#         print("B : ",self.b)

# class C(B):
#     def getC(self,c):
#         self.c=c
#     def putC(self):
#         print("C : ",self.c)

# c1=C()
# c1.getA(10)
# c1.getB(20)
# c1.getC(30)
# c1.putA()
# c1.putB()
# c1.putC()

# Multiple Inheritance..

# class A:
#     def getA(self,a):
#         self.a=a
#     def putA(self):
#         print("A : ",self.a)

# class B:
#     def getB(self,b):
#         self.b=b
#     def putB(self):
#         print("B : ",self.b)

# class C(A,B):
#     def getC(self,c):
#         self.c=c
#     def putC(self):
#         print("C : ",self.c)


# c1=C()
# c1.getA(100)
# c1.getB(200)
# c1.getC(300)
# c1.putA()
# c1.putB()
# c1.putC()

#  Hierarchy Inheritance..

# class A:
#     def getA(self,a):
#         self.a=a
#     def putA(self):
#         print("A : ",self.a)

# class B(A):
#     def getB(self,b):
#         self.b=b
#     def putB(self):
#         print("B : ",self.b)

# class C(A):
#     def getC(self,c):
#         self.c=c
#     def putC(self):
#         print("C : ",self.c)

# class D(A):
#     def getD(self,d):
#         self.d=d
#     def putD(self):
#         print("D : ",self.d)

# b1=B()
# c1=C()
# d1=D()
# b1.getA(10)
# b1.putA()
# b1.getB(20)
# b1.putB()
# c1.getC(30)
# c1.putC()
# d1.getD(40)
# d1.putD()

#  Hybrid Inheritance...

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)

class C(A):
   def getC(self,c):
       self.c=c
   def putC(self):
       print("C : ",self.c)

class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D : ",self.d)


d1=D()

d1.getA(10)
d1.getB(20)
d1.getC(30)
d1.getD(40)
d1.putA()
d1.putB()
d1.putC()
d1.putD()
