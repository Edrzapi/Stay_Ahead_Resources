# ==========================================
# SOLUTION - USER DEFINED CALCULATOR
# USING LAMBDA FUNCTIONS
# ==========================================

# Each value is a lambda: a small anonymous function stored
# like any other dictionary value. No parentheses after the
# lambda here - we are storing behaviour, not calling it yet.
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


# ------------------------------------------
# USER INPUT
# ------------------------------------------

first_number = float(
    input("Enter first number: ")
)

operator = input(
    "Choose +, -, *, /: "
)

second_number = float(
    input("Enter second number: ")
)


# ------------------------------------------
# LOOK UP, THEN CALL
# ------------------------------------------

# 1. membership check handles the EXTRA CHALLENGE: an unknown
#    operator prints a message instead of raising KeyError.
if operator in operations:
    # 2. retrieve the lambda (a function object)...
    operation = operations[operator]
    # 3. ...and NOW call it with the two numbers.
    result = operation(first_number, second_number)
    # 4. print the result
    print(f"Result: {result}")
else:
    print("Invalid operator")


# ------------------------------------------
# Alternative worth showing: dict.get with a fallback lambda
# ------------------------------------------
# operation = operations.get(operator)
# print(f"Result: {operation(first_number, second_number)}"
#       if operation else "Invalid operator")
#
# Stretch thought: division by zero still crashes - a try/except
# ZeroDivisionError around the call is the natural next step.
