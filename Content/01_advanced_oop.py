# PYP2 live demo scratch - 01 advanced oop



print(dir(str))


class Bank:
    def __init__(self, deposit_amount, balance):
        self.deposit_amount = deposit_amount
        self._balance = balance # _Protected

    def __add__(self, other):
        # called when Bank() + something else
        print("__add__ has been called")
        return self.deposit_amount + other.deposit_amount

    def __radd__(self, other):
        # called when something else + Bank()
        print("__radd__ has been called")
        return self.deposit_amount + other

    def __str__(self):
        return f"Your bank account contains: {self.deposit_amount}"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

# bank = Bank(100)
# print(bank.deposit_amount + 50) # -> add // 150
# print(50 + bank) # -> radd // 150
# print(bank.balance)
# print(bank)



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # TODO: Create a getter called salary
    @property
    def salary(self):
        return self._salary


    # TODO: Create a setter for salary
    @salary.setter
    def salary(self, value):
        # Reject values below 0 by raising ValueError
        if value < 0:
            raise ValueError("Salary cannot be negative")
        # Otherwise update _salary
        self._salary = value

employee = Employee("Alice", 30_000)

print(employee.salary)      # Should print 30000

employee.salary = 35_000    # Should work
print(employee.salary)      # Should print 35000

# employee.salary = -100      # Should raise ValueError





class Vehicle:
    # TODO: Constructor should accept a brand
    def __init__(self, brand):
        self.brand = brand

    # TODO: Create a method called move()
    # Print "<brand> is moving"
    def move(self):
        print(f"{self.brand} is moving")


# TODO: Create Car that inherits from Vehicle
class Car(Vehicle, Bank):
    # TODO: Add a method called drive()
    # Print "<brand> is driving"
    def drive(self):
        print(f"{self.brand} is driving")


# Create a Car
car = Car("BMW")

car.move() # inherited
car.drive() # part of child class


# TODO: Test whether car is an instance of Car
print(isinstance(car, Car)) # True

# TODO: Test whether car is also an instance of Vehicle
print(isinstance(car, Vehicle)) # True

# TODO: Test whether Car is a subclass of Vehicle
print(issubclass(Car, Vehicle)) # True



class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
    # Calls the next class in MRO
        super().greet() # Hello from A

class C(A):
    def greet(self):
        print("Hello from C")
    # call the next class in MRO
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")

        # call the next class in MRO
        super().greet()


d = D() #
d.greet()
# calculated by C3 LA
print(D.mro())




