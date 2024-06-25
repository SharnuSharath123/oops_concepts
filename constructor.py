# how constructors are working:

class MyClass:
    def __init__(self):
        print("This is constructor...")

    def m1(self):
        print("Hello!!!")

mc = MyClass()  # invoke constructor automatically
mc.m1()   # method we have call explicitly by using object



# example for constructor have take argument

class MyClass:
    name = "Moni"
    def __init__(self, name):  # constructor expecting one argument
        print(name)
        print(self.name)

mc = MyClass("David")  # passing parameter to the constructor



# example for class employee  

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename 
        self.sal = sal

    def display(self):
        print(self.eid, self.ename, self.sal)

e1 = Emp(101, "bash", 50000)
e1.display()

e2 = Emp(102, "bruce", 60000)
e2.display()
