# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price.
# Use @property to get the price, @price.setter to update it,
# and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Get the price of the product."""
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price of the product."""
        del self._price


# Example Usage
p = Product(100.00)
print(p.price)  # Output: 100.0
p.price = 120.00  # Update the price
print(p.price)  # Output: 120.0
del p.price  # Delete the price
# Uncommenting the line below will raise an error since _price is deleted
# print(p._price)