class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length


len=int(input("Length of rectangle: \n"))
br=int(input("Breadth of rectangle: \n"))
obj=rectangle(len,br)
print("Area of rectangle:",obj.area())
