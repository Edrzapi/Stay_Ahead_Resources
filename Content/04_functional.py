# PYP2 live demo - 04 functional programming
# What we covered: functions as objects, storing functions in data
# structures, monkey patching, and function attributes.


# ---------------------------------------------------------------------
# Warm-up: unique values
# ---------------------------------------------------------------------
# Two tools, one subtle difference:
#   set(...)            - dedupes, but order is NOT guaranteed
#   dict.fromkeys(...)  - dedupes AND preserves first-seen order
#                         (dict keys keep insertion order since 3.7)
def unique_numbers(list_num):
    return list(dict.fromkeys(list_num))


assert unique_numbers([1, 2, 4, 3, 4, 5, 5]) == [1, 2, 4, 3, 5]

# Note from class: list(set(...)) happens to LOOK ordered for small ints,
# but that's luck, not a promise - don't rely on it.


# ---------------------------------------------------------------------
# Functions are objects - store them in a dict and pick one at runtime
# ---------------------------------------------------------------------
def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sub(a, b):
    return a - b


# The dict values are the FUNCTIONS THEMSELVES (no parentheses -
# we're storing them, not calling them). Two keys can share one function:
operator = {
    "add": add,
    "+": add,
    "mul": mul,
    "sub": sub,
    "div": div,
}

# The lookup-then-call pattern (uncomment to try interactively):
# choice = input("Give me an operation: ")
# operation = operator[choice]     # fetch the function object
# result = operation(5, 6)         # NOW call it
# print(result)


# ---------------------------------------------------------------------
# 1. A function is a value - assign it to another name
# ---------------------------------------------------------------------
out = print          # 'out' and 'print' now point at the SAME function
out('Hello')


# ---------------------------------------------------------------------
# 2. Monkey patching - replacing a function at runtime
# ---------------------------------------------------------------------
# Because module attributes are just names pointing at function objects,
# we can point one at our own function. Powerful for testing (fake a
# random value, freeze a clock) - dangerous anywhere else, because
# EVERY caller of random.random() is now affected.
import random

random.random = lambda: 0.5
print(random.random())   # 0.5 - every time


# ---------------------------------------------------------------------
# 3. Functions can carry attributes - they're objects like any other
# ---------------------------------------------------------------------
def greeting(): pass


greeting.language = 'English'
greeting.calls = 0
print(greeting.language)     # English

# Watch this: defining a new 'add' rebinds the NAME 'add'...
def add(): pass


add.number_one = 1
print(add.number_one)        # 1

# ...but the operator dict still holds a reference to the ORIGINAL
# two-argument add - names and objects are separate things:
print(operator["add"](2, 3))   # 5
