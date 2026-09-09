import math


# =========================================================
# 1. CIRCLE
# =========================================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius


# =========================================================
# 2. BANK LOAN
# =========================================================

class BankLoan:
    def __init__(self, amount, term, interest_rate):
        self.amount = amount
        self.term = term
        self.interest_rate = interest_rate

    @property
    def total_repayable(self):
        return (
            self.amount * self.interest_rate / 100
            + self.amount
        )

    @property
    def monthly_repayment(self):
        return self.total_repayable / (self.term * 12)


# =========================================================
# 3. PRODUCT
# =========================================================

class Product:
    def __init__(self, product_id, name, price):
        # Private-ish attributes
        self._product_id = product_id
        self._name = name
        self._price = price

    # Read-only properties
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    # Products can be compared by ID
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False

        return self.product_id == other.product_id

    def __hash__(self):
        return hash(self.product_id)

    def __repr__(self):
        return (
            f"Product("
            f"{self.product_id!r}, "
            f"{self.name!r}, "
            f"{self.price!r})"
        )


# =========================================================
# 4. BASKET
# =========================================================

class Basket:
    def __init__(self):
        # Internal dictionary:
        # Product -> quantity
        self._items = {}

    @property
    def contents(self):
        # Return a COPY so callers cannot
        # directly modify the real basket
        return self._items.copy()

    def add_product(self, product, quantity=1):

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        # Prevent duplicate Product keys.
        # If already present, increase quantity instead.
        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    def remove_product(self, product):
        if product in self._items:
            del self._items[product]

    @property
    def total_products(self):
        # Sum quantities
        return sum(self._items.values())

    @property
    def total_price(self):
        return sum(
            product.price * quantity
            for product, quantity in self._items.items()
        )


# =========================================================
# 5. INVENTORY
# =========================================================

class Inventory:
    def __init__(self, filename):
        self.filename = filename

    def _load_inventory(self):
        inventory = {}

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    product_id, quantity = line.strip().split(",")

                    inventory[product_id] = int(quantity)

        except FileNotFoundError:
            pass

        return inventory

    def _save_inventory(self, inventory):

        with open(self.filename, "w") as file:
            for product_id, quantity in inventory.items():
                file.write(f"{product_id},{quantity}\n")

    def get_stock(self, product):

        inventory = self._load_inventory()

        return inventory.get(product.product_id, 0)

    def reduce_stock(self, product, quantity):

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        inventory = self._load_inventory()

        current_stock = inventory.get(
            product.product_id,
            0
        )

        if quantity > current_stock:
            return False

        inventory[product.product_id] = (
            current_stock - quantity
        )

        self._save_inventory(inventory)

        return True


# =========================================================
# 6. COLUMN / SERIES-LIKE CLASS
# =========================================================

class Column:
    def __init__(self, data):
        self._data = list(data)

    @property
    def data(self):
        return self._data.copy()

    def _check_numeric(self):

        if not all(
            isinstance(value, (int, float))
            for value in self._data
        ):
            raise TypeError(
                "Column must contain numeric data"
            )

    def min(self):
        self._check_numeric()
        return min(self._data)

    def max(self):
        self._check_numeric()
        return max(self._data)

    def mean(self):
        self._check_numeric()

        if not self._data:
            raise ValueError("Cannot calculate mean of empty column")

        return sum(self._data) / len(self._data)

    def __repr__(self):
        return f"Column({self._data!r})"


# =========================================================
# 7. TABLE / DATAFRAME-LIKE CLASS
# =========================================================

class Table:
    def __init__(self, data):

        # Convert every list into a Column object
        self._columns = {
            name: Column(values)
            for name, values in data.items()
        }

    def __getitem__(self, column_name):
        # Allows:
        # table["price"]
        return self._columns[column_name]

    @property
    def columns(self):
        return list(self._columns.keys())

# =========================================================
# 7. DISCUSSION: Should baskets update the inventory?
# =========================================================
# No. A basket represents what the customer INTENDS to buy;
# the inventory tracks what the store actually HAS. Checking and
# updating stock is a separate responsibility (single-responsibility
# principle) and belongs to a checkout/order process that uses BOTH
# objects. Stock should only change when an order is confirmed,
# not while items sit in a basket.

# =========================================================
# 8. DISCUSSION: What other classes might be required?
# =========================================================
# Customer (identity, addresses), Order (a confirmed basket with a
# date, status, and payment reference), Checkout/OrderService
# (coordinates basket + inventory + payment), Payment, and perhaps
# Catalogue (searchable collection of products).
