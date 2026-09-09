class Vehicle:
    # Constructor accepts a brand
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"{self.brand} is moving")


# Car inherits from Vehicle
class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving")


# Create a Car
car = Car("BMW")

car.move()   # inherited from Vehicle
car.drive()  # defined on Car


# car is an instance of Car
print(isinstance(car, Car))        # True

# car is ALSO an instance of Vehicle (inheritance is an IS-A relationship)
print(isinstance(car, Vehicle))    # True

# Car is a subclass of Vehicle
print(issubclass(Car, Vehicle))    # True
