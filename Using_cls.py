# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0
    # Class variable to keep track of the number of instances

    def __init__(self):
        Counter.count += 1
        # Increment the count each time on instance is created

    @classmethod
    def get_count(cls):
        return cls.count
    # Class method to return the current count of instances

    def __str__(self):
        return f"Counter: {self.get_count()} instances created."


# Example Usage
c1 = Counter()
c2 = Counter()
c3 = Counter()
print(c1)  # Output: Counter: 3 instances created.
print(c2)
print(c3)
