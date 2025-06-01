# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception if age < 18.
# Handle it with try...except.
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        print(f"InvalidAgeError: {self.message}")


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted.")


# Example Usage
try:
    age = int(input("Enter your age: "))
    check_age(age)

except InvalidAgeError as e:
    print(e.message)



