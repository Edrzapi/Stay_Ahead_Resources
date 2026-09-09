class Vehicle:
    vehicle_count = 0

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        Vehicle.vehicle_count += 1

    # Class method: receives the CLASS (cls), not an instance.
    # An alternative constructor - builds a Vehicle from a string.
    @classmethod
    def from_string(cls, vehicle_data):
        brand, year = vehicle_data.split(",")
        return cls(brand, int(year))

    # Static method: receives neither self nor cls.
    # A utility that belongs with the class but needs no instance data.
    @staticmethod
    def valid_registration(registration):
        return isinstance(registration, str) and len(registration) >= 2


# Use the class method
car = Vehicle.from_string("BMW,2025")

print(car.brand)   # BMW
print(car.year)    # 2025


# Use the static method
print(Vehicle.valid_registration("AB12 XYZ"))  # True
print(Vehicle.valid_registration(""))          # False
