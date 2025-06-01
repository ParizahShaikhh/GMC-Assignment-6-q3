# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


m = MathUtils()
result = m.add(5, 3)
print(result)  # Output: 8
# Accessing the static method without creating an instance (Preferred way)
result_static = MathUtils.add(10, 20)
print(result_static)  # Output: 30
# Demonstrating that no class or instance variables are used
# print(MathUtils.__dict__)  # Output: {'__module__': '__main__', 'add': <staticmethod object at ...>, '__dict__': <attribute '__dict__' of 'MathUtils' objects>, '__weakref__': <attribute '__weakref__' of 'MathUtils' objects>, '__doc__': None}
# print(m.__dict__)  # Output: {}  # No instance variables
# print(MathUtils.add.__self__)  # Output: None  # Static method does not have a self reference
