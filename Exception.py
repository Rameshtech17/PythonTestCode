try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    print(a / b)
except Exception as error:
    print("Error :", error)
except ValueError as Error:
    print("Error: ", Error)
finally:
    print("Final")

##########################################
try:
    print("Hello")
    a = int(input("Enter A : "))
except:
    print("Something Went Wrong")
else:
    print("Nothing Went Wrong")

##########################################
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


# try:
#     fh = open("text.txt", "r")
#     fh.write("This is my test file for exception handling!!")
# except IOError:
#     print("Error: can\'t find file or read data")
# else:
#     print("Written content in the file successfully")

#
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')
