"""--------------------
Static method
---------------------"""
# a static method is a method that do not operate on an instance (self) or class

class Math:
    @staticmethod
    def add(a, b):  # add will not change values in the class math
        return a + b

print(Math.add(3, 5))  # Output: 8




"""--------------------
Class method
---------------------"""
# a class method define  a method that operate on the class itself (cls) instead of an instance.

class Employee:
    company = "TechCorp"

    def __init__(self):
        pass

    @classmethod
    def change_company(cls, new_company):  # change value for the class but not self
        cls.company = new_company


e = Employee()
f = Employee()

# will change for each instance of the class (e and f)
Employee.change_company("InnoTech")

print(Employee.company)  # Output: InnoTech
print(e.company)
print(f.company)



"""--------------------
Property
---------------------"""

# Turns a method into a read-only attribute
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self): # acces sekf but doesn't modify it
        return 3.14 * (self.radius ** 2)

c = Circle(5)
print(c.area)  # Output: 78.5


