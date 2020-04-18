class Base:
    def __init__(self,A,B):
        self.a=A
        self.b=B

    def Add(self):
        print("Add : {}".format(self.a + self.b))

    def Sub(self):
        print("Sub : {}".format(self.a - self.b))

class Der1(Base):
    def __init__(self,A,B):
        self.a=A
        self.b=B
    def Mul(self):
        print("Mul : {}".format(self.a * self.b))

    def Div(self):
        print("Div : {}".format(self.a / self.b))

class Der(Der1):
    def __init__(self,A,B):
        self.a =A
        self.b =B

    def Mod(self):
        print("Mod : {}".format(self.a % self.b ))


a1=Der(5,3)
a1.Add()
a1.Sub()
a1.Mul()
a1.Div()
a1.Mod()