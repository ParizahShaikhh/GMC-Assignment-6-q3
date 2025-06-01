# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) # Call the base class constructor
        self.subject = subject

    def __str__(self):
        return f"Teacher(Name: {self.name}, Subject: {self.subject})"


# Example Usage
t = Teacher("John Doe", "Mathematics")
print(t)  # Output: Teacher(Name: John Doe, Subject: Mathematics)
