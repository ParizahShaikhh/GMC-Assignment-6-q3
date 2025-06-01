# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
# Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    # Define the greet method to be added to the class
    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person(Name: {self.name})"


# Example Usage
person = Person("John")
print(person.greet())  # Output: Hello from Decorator!
print(person)  # Output: Person(Name: John)


# Ready for more challenges, or want to experiment with decorators that:
# Log method calls?
# Modify attributes?
# Wrap class methods?
