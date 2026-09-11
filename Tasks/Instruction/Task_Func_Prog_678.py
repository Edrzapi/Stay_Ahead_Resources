# ==========================================================
# FUNCTIONAL PROGRAMMING TASKS 6, 7 AND 8
# ==========================================================


# ----------------------------------------------------------
# TASK 6
#
# Create a higher-order function called process_file().
#
# It should accept:
#   1. a filename
#   2. a function
#
# Open the file and apply the function to each line.
# ----------------------------------------------------------

def process_file(filename, function):
    # TODO:
    pass


# ----------------------------------------------------------
# TASK 7
#
# Call process_file() and pass in a lambda function.
#
# The lambda should print each line to the screen.
# ----------------------------------------------------------

# TODO:
# process_file(...)



# ----------------------------------------------------------
# TASK 8
#
# The function below is tightly coupled to
# take_from_inventory().
#
# Refactor it so that the inventory behaviour can be
# passed into add_to_basket() as a function instead.
# ----------------------------------------------------------

def take_from_inventory(product, qty):
    print(f"Removing {qty} x {product} from inventory")


def add_to_basket(basket, product, qty):
    take_from_inventory(product, qty)

    if product in basket:
        basket[product] += qty
    else:
        basket[product] = qty


# TODO:
# Refactor add_to_basket() so that take_from_inventory
# is not hard-coded inside it.



# ----------------------------------------------------------
# TEST DATA
# ----------------------------------------------------------

basket = {}


# TODO:
# Call add_to_basket() using:
#
# product = "Laptop"
# qty = 1
#
# Pass the inventory function into add_to_basket()
# once you have refactored it.


print(basket)