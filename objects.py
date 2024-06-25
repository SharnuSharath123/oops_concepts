# example for global, class and local variables

i,j = 15,25  # global variables
class MyClass:
    a,b = 10,20  # class variables
    def add(self, x, y):
        print(x+y)  # local variables
        print(self.a+self.b)   # class variables
        print(i+j)  # global variables

mc = MyClass()
mc.add(30,40)



# another example for global, class and local variables

a,b = 15,25  # global variables
class MyClass:
    a,b = 10,20  # class variables
    def add(self, a, b):
        print(a+b)  # local variables
        print(self.a+self.b)   # class variables
        print(globals()['a']+globals()['b'])  # global variables

mc = MyClass()
mc.add(100,200)



# example for one class can have multiple objects

class MyClass:
    def display(self, name):
        print("This is display method")
        print(name)

obj1 = MyClass()
obj1.display("Marsh")

obj2 = MyClass()
obj2.display("Mitchell")
