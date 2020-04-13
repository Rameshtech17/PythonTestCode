class calc:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def add(self):
        return self.A + self.B

    def sub(self):
        return self.A - self.B

    def mul(self):
        return self.A * self.B

    def div(self):
        return self.A / self.B


a = int(input("Enter A value : \n"))
b = int(input("Enter B value : \n"))

c = calc(a, b)
print("Add :", c.add())
print("Sub :", c.sub())
print("Mul :", c.mul())
print("Div :", c.div())
