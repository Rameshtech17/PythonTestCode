# Duck Typiing
class math1:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def add(self):
        print("Add  : {} ".format(self.A + self.B))

class math2:
    def __init__(self, A, B):
        self.a = A
        self.b = B

    def add(self):
        print("Add : {}".format(self.a + self.b))

class fun:
    def calc(self, a1):
        a1.add()

a1 = math1(2, 3)
a2 = math2(5, 6)

f1 = fun()
f1.calc(a1)
f1.calc(a2)

# Operator Overloading
class Class:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return 'A :{} B :{}'.format(self.a + other.a, self.b + other.b)
    def __str__(self):
        return '{} {}'.format(self.a, self.b)

c1=Class(1,2)
c2=Class(1,2)
c3= c1+c2
print(c3)
print(c1)

# Method Overloading
class A:
    def add(self,A=None,B=None,C=None):
        D = 0
        if A != None and B != None and C != None:
            D = A + B + C
        elif A != None and B != None:
            D = A + B
        else:
            D = A
        return  D


A1=A()
print (A1.add(2,3,4))  # 3 argument
print (A1.add(2,3))  # 2 Argument
print (A1.add(2))  # 1 Argument

# Method Overriding

class base:
    def Print(self):
        print("Printing Base Class Data")
class Driv(base):
    pass
B1= Driv()
B1.Print()

class base1:
    def Print(self):
        print("Printing Base Class Data")
class Driv1(base1):
    def Print(self):
        print("Printing Derived Class Data")
B1= Driv1()
B1.Print()



