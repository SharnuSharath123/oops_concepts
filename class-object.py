# normal class and object example
class MyClass:
    def myfun(self):
        print("Hello", end=" ")

    def display(self):
        print("World!!!")

m1 = MyClass()
m1.myfun()
m1.display()



# instance and static method example

class MyClass:
    def m1(self):  # this self keyword referring as class
        print("This is instance method...")

    @staticmethod
    def m2(self, num):  # this self keyword referring as a parameter
        print(self, num) # in static method self keyword also, contain value


mc = MyClass()
mc.m1()
mc.m2(100,120)

