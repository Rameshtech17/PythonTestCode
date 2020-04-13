num=int(input("Enter number of elements:"))
val=[]
for i in range(1,num+1):
    a=int(input("Enter element:"))
    val.append(a)
val.sort()
print("After Sort{}".format(val))
print("Largest element is:",val[num-1])