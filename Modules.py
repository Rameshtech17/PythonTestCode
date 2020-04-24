from math import pi
import calendar

c=calendar.Calendar()
print(calendar.prcal(2019))
# print(iterweekdays())
print(c.itermonthdates(2000, 1))

r = int(input("Enter Radius:"))

a = pi * r

print("Area of circle :", a)
