# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name.
# Show that it affects all instances.

class Bank:
    bank_name = "Global Bank"  # Class variable
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        # Class method to change the bank name

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name


b = Bank()
# Example Usage
print(b.get_bank_name())  # Output: Global Bank
b.change_bank_name("International Bank")
print(b.get_bank_name())  # Output: International Bank
# Show that it affects all instances
b2 = Bank()
print(b2.get_bank_name())  # Output: International Bank
# Changing the bank name through another instance
b2.change_bank_name("National Bank")
print(b.get_bank_name())  # Output: National Bank