# ==========================================================
# SOLUTION - FUNCTIONAL PROGRAMMING TASKS 6, 7 AND 8
# ==========================================================


# ----------------------------------------------------------
# TASK 6 - process_file(): a higher-order function
# ----------------------------------------------------------
# The FILE handling stays fixed; the varying part (what to do
# with each line) arrives as a function parameter.

def process_file(filename, function):
    with open(filename) as file:      # with = file closes itself
        for line in file:
            function(line.rstrip("\n"))   # strip the newline, then delegate


# ----------------------------------------------------------
# TASK 7 - call it with a lambda that prints each line
# ----------------------------------------------------------

# Create a small demo file so this solution runs anywhere:
with open("demo_lines.txt", "w") as f:
    f.write("first line\nsecond line\nthird line\n")

process_file("demo_lines.txt", lambda line: print(line))

# The same machinery immediately does other jobs - only the
# lambda changes, process_file() is untouched:
process_file("demo_lines.txt", lambda line: print(line.upper()))
process_file("demo_lines.txt", lambda line: print(len(line)))


# ----------------------------------------------------------
# TASK 8 - decouple add_to_basket from take_from_inventory
# ----------------------------------------------------------

def take_from_inventory(product, qty):
    print(f"Removing {qty} x {product} from inventory")


# BEFORE: take_from_inventory was hard-coded inside add_to_basket,
# so the basket could never be used with a different inventory
# system (or none at all, e.g. in a test).
#
# AFTER: the inventory behaviour is a PARAMETER. add_to_basket
# no longer knows or cares which inventory function it calls.

def add_to_basket(basket, product, qty, inventory_action):
    inventory_action(product, qty)

    if product in basket:
        basket[product] += qty
    else:
        basket[product] = qty


# ----------------------------------------------------------
# TEST DATA
# ----------------------------------------------------------

basket = {}

# Pass the real inventory function in - note: no parentheses,
# we hand over the function itself, add_to_basket calls it.
add_to_basket(basket, "Laptop", 1, take_from_inventory)

print(basket)     # {'Laptop': 1}

# Why this matters - the same basket code now works with ANY
# inventory behaviour, e.g. a do-nothing lambda in a unit test:
add_to_basket(basket, "Mouse", 2, lambda product, qty: None)
print(basket)     # {'Laptop': 1, 'Mouse': 2}
