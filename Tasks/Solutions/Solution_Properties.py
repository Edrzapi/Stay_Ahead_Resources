class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # Getter: read access via employee.salary
    @property
    def salary(self):
        return self._salary

    # Setter: validates before updating _salary
    @salary.setter
    def salary(self, value):
        # Reject values below 0 by raising ValueError
        if value < 0:
            raise ValueError("Salary cannot be negative")
        # Otherwise update _salary
        self._salary = value


employee = Employee("Alice", 30_000)

print(employee.salary)      # 30000

employee.salary = 35_000    # Works - setter runs the validation
print(employee.salary)      # 35000

# Uncomment to see the validation fire:
# employee.salary = -100    # Raises ValueError("Salary cannot be negative")
