def Oddeven(x):

    if x % 2 == 0:
        print("{} is Even".format(x))
    else:
        print("{} is  Odd".format(x))
    return 3


def function(x,y):
    print("X = {}, Y={}".format(x,y))
    # print("Y = {}".format(y))


a = int(input("Enter number"))
b = int(input("Enter number"))

m= Oddeven(a)
n=Oddeven(b)

function(a,b)
function(x=a,y=b)
function(y=a,x=b)
print("M is {}".format(m))