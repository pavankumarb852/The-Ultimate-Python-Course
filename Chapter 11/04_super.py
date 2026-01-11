class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)




############

# Base (Parent) class
class Employee:
    def __init__(self):
        # Constructor of Employee class
        print("Constructor of Employee")

    # Class variable
    a = 1


# Child class inheriting from Employee
class Programmer(Employee):
    def __init__(self):
        # Constructor of Programmer class
        print("Constructor of Programmer")

    # Class variable
    b = 2


# Child class inheriting from Programmer (Multilevel Inheritance)
class Manager(Programmer):
    def __init__(self):
        # Calling parent class (Programmer) constructor
        super().__init__()

        # Constructor of Manager class
        print("Constructor of Manager")

    # Class variable
    c = 3


# Creating an object of Manager class
o = Manager()

# Accessing class variables inherited from all parent classes
print(o.a, o.b, o.c)


Output
Constructor of Programmer
Constructor of Manager
1 2 3

