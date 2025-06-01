# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes.
# Apply it to a function say_hello().

def log_function_call(func):
    """
    Decorator to log function calls with their arguments and return values.
    """
    def wrapper(*args, **kwargs):
        print("Function is being called")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function_call
def say_hello(name):
    """
    Function that returns a greeting message.
    """
    return f"Hello, {name}!"


print(say_hello(input("Enter your name: ")))  # Calls the decorated function

# want to add:
# Logging return values too
# Timing how long a function takes
# Stacking multiple decorators
