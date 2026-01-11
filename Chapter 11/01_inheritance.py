class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)



########

# Parent class
class Employee:
    # Class variable (shared by all Employee objects)
    company = "ITC"

    # Instance method to display employee details
    def show(self):
        print(
            f"The name of the Employee is {self.name} "
            f"and the salary is {self.salary}"
        )


# Child class inheriting from Employee
class Programmer(Employee):
    # Overriding the class variable from Employee
    company = "ITC Infotech"

    # New method specific to Programmer class
    def showLanguage(self):
        print(
            f"The name is {self.name} "
            f"and he is good with {self.language} language"
        )


# Creating an object of Employee
a = Employee()

# Creating an object of Programmer
b = Programmer()

# Printing company names
# a uses Employee.company
# b uses Programmer.company (overridden value)
print(a.company, b.company)
