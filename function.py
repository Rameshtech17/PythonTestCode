def Oddeven(x):
    if x % 2 == 0:
        print("{} is Even".format(x))
    else:
        print("{} is  Odd".format(x))
    return 3


def function(x, y):
    print("X = {}, Y={}".format(x, y))
    # print("Y = {}".format(y))


a = int(input("Enter number"))
b = int(input("Enter number"))

m = Oddeven(a)
n = Oddeven(b)

function(a, b)
function(x=a, y=b)
function(y=a, x=b)
print("M is {}".format(m))


########################################
# Default argument
def fun(a=4, b=5):
    return a + b


print(fun())


def prim(num):
    n = num - 1
    for i in range(2, n):
        if num % i == 0:
            return False
    else:
        return True


print(prim(7))


########################################
#  Keyword argument

def Fun_key(a, b):
    print("A: ", a)
    print("B: ", b)


Fun_key(2, 3)
Fun_key(a=3, b=2)


#########################################
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok('OK to overwrite the file?', 2)
