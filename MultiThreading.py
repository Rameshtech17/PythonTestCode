from time import sleep
from threading import *


class A(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(10):
            print("Welcome")
            sleep(1)


obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()

obj2.join()
obj1.join()

print("Bye")
