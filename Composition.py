# 13. Composition
# Assignment:
# Create a class Engine and a class Car.
# Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def drive(self):
        self.engine.start()


# Example Usage
engine = Engine()
car = Car("Toyota", engine)
car.drive()  # Starts the engine
