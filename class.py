class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return (self.breadth * self.length) / 2


#  class varriables
class var:
    class_variable = 5

    def __init__(self):
        self.instance_variable = 10


# Class Methods
class methods:
    def __init__(self, A, B):
        self.a = A
        self.b = B

    def add(self):
        print("In instance Method  a+b ={}".format(self.a + self.b))

    @classmethod
    def class_Method(cls):
        print('This is Class Method ')

    @staticmethod
    def Static_Method(a, b):
        print("This is Static Method  a+b={} ".format(a + b))


# class inside class
class Class:
    def __init__(self, name, age, ph, mi):
        self.name = name
        self.age = age
        self.cls = self.inside_class(ph, mi)

    def show(self):
        print(self.name, self.age)
        self.cls.show()

    class inside_class:
        def __init__(self, phone, mail):
            self.phone = phone
            self.mail = mail

        def show(self):
            print(self.phone, self.mail)


len = int(input("Length of rectangle: \n"))
br = int(input("Breadth of rectangle: \n"))
obj = rectangle(len, br)
print("Area of rectangle:", obj.area())

obj1 = var()
obj2 = var()
print("Object_1 Class variable: {} Instance variable: {}".format(obj1.class_variable, obj1.instance_variable))
print("Object_2 Class variable: {} Instance variable: {}".format(obj2.class_variable, obj2.instance_variable))
var.class_variable = 30
print("Object_1 Class variable: {} Instance variable: {}".format(obj1.class_variable, obj1.instance_variable))
print("Object_2 Class variable: {} Instance variable: {}".format(obj2.class_variable, obj2.instance_variable))

obj3 = methods(3, 5)
obj3.add()
methods.class_Method()
methods.Static_Method(2, 3)

obj4 = Class("Raj", 20, "913453523", "test@gmail.com")
obj4.show()
