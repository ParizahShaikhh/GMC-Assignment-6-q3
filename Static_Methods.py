# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return f"{(c * 9/5) + 32} Fahrenheit"

    @staticmethod
    def fahrenheit_to_celsius(f):
        return f"{(f - 32) * 5/9} Celsius"


# Example Usage
temp_converter = TemperatureConverter()
print(temp_converter.celsius_to_fahrenheit(25))  # Output: 77.0
print(temp_converter.fahrenheit_to_celsius(77))  # Output: 25.0
