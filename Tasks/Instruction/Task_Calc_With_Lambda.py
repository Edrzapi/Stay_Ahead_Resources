# ==========================================
# MINI TASK - USER DEFINED CALCULATOR
# USING LAMBDA FUNCTIONS
# ==========================================


# TODO:
# Create a dictionary called operations.
#
# Each key should be an operator:
# "+", "-", "*", "/"
#
# Each value should be a lambda function
# that accepts two values and performs
# the correct calculation.

operations = {
    # "+": ...
    # "-": ...
    # "*": ...
    # "/": ...
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
# TASK
# ------------------------------------------

# TODO:
# 1. Check whether the operator exists
#    inside the operations dictionary.
#
# 2. Retrieve the correct lambda function.
#
# 3. Call the function using:
#       first_number
#       second_number
#
# 4. Print the result.
#
# Example:
#
# Enter first number: 10
# Choose +, -, *, /: *
# Enter second number: 5
#
# Result: 50


# ------------------------------------------
# EXTRA CHALLENGE
# ------------------------------------------

# If the user enters an invalid operator,
# such as:
#
# %
#
# print:
#
# Invalid operator
#
# instead of allowing the program to crash.