import sys

a=int(sys.argv[1])
b=int(sys.argv[2])
c=a+b
print(c)

z=0
x=len(sys.argv)
print("Number of argument passed: " ,x)
for y in range(1,x):
    z+=int(sys.argv[y])
print(z)

