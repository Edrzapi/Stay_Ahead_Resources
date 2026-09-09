class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # TODO: Create a getter called salary


    # TODO: Create a setter for salary
    # Reject values below 0 by raising ValueError
    # Otherwise update _salary


employee = Employee("Alice", 30_000)

print(employee.salary)      # Should print 30000

employee.salary = 35_000    # Should work
print(employee.salary)      # Should print 35000

employee.salary = -100      # Should raise ValueError
