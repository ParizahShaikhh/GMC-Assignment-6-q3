# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# 
# a public variable name,
# 
# a protected variable _salary, and
# 
# a private variable __ssn.
# 
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn})"


# Example Usage

e = Employee("John Doe", 50000, "123-45-6789")
print(e.name)  # Accessing public variable
print(e._salary)  # Accessing protected variable (not recommended, but possible)
print(e._Employee__ssn)  # Accessing private variable (not recommended, but possible)

print(e)  # Output: Employee(Name: John Doe, Salary: 50000, SSN: 123-45-6789)

# print(e.__ssn)  # Raises AttributeError: 'Employee' object has no attribute '__ssn'