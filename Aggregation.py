# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Department:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Employee(Name: {self.name}, Department: {self.department.name})"


# Example Usage
department = Department("HR")
employee = Employee("John Doe", department)
print(employee)

# del department  # Deleting the department object

# print(employee)  # Output: Employee(Name: John Doe, Department: HR)
# Note: The department object is deleted, but the employee still holds a reference to it.
