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
