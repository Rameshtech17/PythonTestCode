num = [1, 2, 3, 4, 5, 6]
print(num)
num.extend([7, 8, 9])  # add 7,8,9 to list
print(num)
print(num[3])  # printing the value of index[3]
print(num[3:])  # printing value between index[3] to last value of list
print(num[3:8])  # printing value between index[3] to index[8]
print(num[-6:-1])  # printing value between index[3] to index[8]
num1 = num.copy()  # copy list
print(num1)
num1.append(10)  # add number 10 list

print(num1)
print(num1.pop())  # remove tha last element of list
print(num1)
num1.remove(4)  # delete tha value 4 in list
print(num1)

num1.insert(3, 4)  # insert value 4 in index [3]
print(num1)
del num1[6:8]  # Delete the value between index[6] to index[8]
print(num1)

print(min(num1))
print(max(num1))
num2 = list(range(0, 20, 3))
print(num2)

#  search

i = int(input("Enter the number of elements in a list :"))

List = []
Pos = 0

for j in range(0, i):
    k = int(input())
    List.append(k)  # add the value in end of list
n = int(input("Enter The value to search : "))


def Leaner_Search(list, N):
    print(list)
    for I in range(0, len(list)):
        if list[I] == N:
            globals()['Pos'] = I
            return True
    return False


def Binary_Search(list, N):
    print(list)
    L = 0
    U = len(list) - 1
    while L <= U:
        mid = (L + U) // 2

        if list[mid] == N:
            globals()['Pos'] = mid
            return True
        else:
            if list[mid] < N:
                L = mid + 1
            else:
                U = mid + 1
    return False


SList = sorted(List)

opt = int(input(" 1. Leaner Search 2. Binary Search \n Select Search Option "))

if opt == 2:
    if Binary_Search(SList, n):
        print("Value found At :", Pos + 1)
    else:
        print("Value not found :")
elif opt == 1:
    if Leaner_Search(List, n):
        print("Value found At :", Pos + 1)
    else:
        print("Value not found :")
else:
    print("Select correct option")


#   Nested List
nlist = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print("Nested List")
print(nlist)
print(nlist[0])
print((nlist[0][0]))
print(nlist[1])
print(nlist[1][0])
print(nlist[2])
print(nlist[2][0])