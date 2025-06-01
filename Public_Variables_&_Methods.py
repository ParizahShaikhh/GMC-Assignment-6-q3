# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.
class Car:
    brand = "Toyota"
    # Public variable

    def start(self):
        return f"{self.brand} is starting."
    # Public method


# Example Usage
my_car = Car()

print(my_car.brand)  # Output: Toyota
print(my_car.start())  # Output: Toyota is starting.
# Accessing public variable and method from outside the class
