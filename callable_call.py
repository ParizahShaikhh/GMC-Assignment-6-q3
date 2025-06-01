# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor.
# Define a __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# Example Usage
multiplier = Multiplier(float(input("Enter a factor: ")))  # Create an instance with a factor
result = multiplier(float(input("Enter a value: ")))  # Calls the __call__ method
callable_result = callable(multiplier)  # Checks if multiplier is callable
# callable_result = callable(Multiplier)
print(result)  # Output: 15
print(callable_result)  # Output: True

# You could also test
# callable(Multiplier)
# this would return True
# because classes in Python are also callable (to create instances).
