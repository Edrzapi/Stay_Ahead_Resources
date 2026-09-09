class Vehicle:
    vehicle_count = 0

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        Vehicle.vehicle_count += 1

    # TODO: Create a class method called from_string
    # Split vehicle_data into brand and year
    # Return a new Vehicle using cls(...)
    #
    # Example input: "BMW,2025"


    # TODO: Create a static method called valid_registration
    # Return True if the registration:
    # - is a string
    # - contains at least 2 characters


# Use the class method
car = Vehicle.from_string("BMW,2025")

print(car.brand)   # BMW
print(car.year)    # 2025


# Use the static method
print(Vehicle.valid_registration("AB12 XYZ"))  # True
print(Vehicle.valid_registration(""))          # False
