num=int(input("Enter the number of elements: "))
a=[]
for i in range(0,num):
    val=int(input("Enter element: "))
    a.append(val)
avg=sum(a)/num
print("Number is {}".format(a))
print("Average of the list  {}",format(round(avg)))