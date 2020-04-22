String = "WELCOME"
for i in String:
    print(i)

for x in range(1,10,1):
    print(x)

for y in range(10,0,-1):
    print(y)

for a in range(5):
    for b in range(5-a):
        print("* ",end="")
    print(" ")



for a in range(6):
    for b in range(a):
        print("* ",end="")
    print(" ")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
