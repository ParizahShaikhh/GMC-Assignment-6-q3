# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.
class A:
    def show(self):
        print("A's show method")


class B(A):
    def show(self):
        print("B's show method")
        super().show()


class C(A):
    def show(self):
        print("C's show method")
        super().show()


class D(B, C):
    def show(self):
        print("D's show method")
        super().show()


# Example Usage
mro = D()
mro.show()
