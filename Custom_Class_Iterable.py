# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number.
# Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# Example Usage
i = Countdown(5)
for number in i:
    print(number)  # Output: 4, 3, 2, 1, 0
