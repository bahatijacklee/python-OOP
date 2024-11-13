# Define a base class for Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Define a Car class that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving... 🚗")

# Define a Plane class that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying... ✈️")

# Create objects and test polymorphism
vehicles = [Car(), Plane()]

for vehicle in vehicles:
    vehicle.move()  # Each object calls its own move method
