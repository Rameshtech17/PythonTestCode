num = [1, 2, 3, 4, 5, 6]
print(num)
num.extend([7, 8, 9])  # add 7,8,9 to list
print(num)
print(num[3])  # printing the value of index[3]
print(num[3:])  # printing value between index[3] to last value of list
print(num[3:8])  # printing value between index[3] to index[8]
print(num[-6:-1])  # printing value between index[3] to index[8]
num1=num.copy()  # copy list
print(num1)
num1.append(10)  # add number 10 list

print(num1)
print(num1.pop())  # remove tha last element of list
print(num1)
num1.remove(4)  # delete tha value 4 in list
print(num1)

num1. insert(3,4)  # insert value 4 in index [3]
print(num1)
del num1[6:8]  # Delete the value between index[6] to index[8]
print(num1)

