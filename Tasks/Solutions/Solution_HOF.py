prices = [25, 80, 120, 15, 300, 60]

# The task file has three near-identical functions: each loops over
# prices and keeps the ones matching a condition. Only the CONDITION
# differs - which is exactly the situation higher-order functions solve:
# pass the varying part in as a function.


# ---------------------------------------------------------------------
# Option 1: filter() + lambda
# ---------------------------------------------------------------------
# filter(condition, sequence) keeps items where condition(item) is True.
# The lambda IS the varying part; the looping is filter's job.

expensive = list(filter(lambda p: p >= 100, prices))
cheap     = list(filter(lambda p: p < 50, prices))
mid_range = list(filter(lambda p: 50 <= p < 100, prices))

print(expensive)   # [120, 300]
print(cheap)       # [25, 15]
print(mid_range)   # [80, 60]


# ---------------------------------------------------------------------
# Option 2: one higher-order function of our own
# ---------------------------------------------------------------------
# Same idea without filter(): the condition arrives as a parameter.
# Three functions collapse into one.

def get_prices(prices, condition):
    return [price for price in prices if condition(price)]


print(get_prices(prices, lambda p: p >= 100))       # expensive
print(get_prices(prices, lambda p: p < 50))         # cheap
print(get_prices(prices, lambda p: 50 <= p < 100))  # mid-range


# ---------------------------------------------------------------------
# Option 3 (stretch): a function FACTORY
# ---------------------------------------------------------------------
# make_range_check returns a new function each time - a closure that
# remembers its bounds. Useful when the same condition is reused a lot.

def make_range_check(low, high=None):
    if high is None:
        return lambda p: p >= low
    return lambda p: low <= p < high


is_expensive = make_range_check(100)
is_mid_range = make_range_check(50, 100)

print(list(filter(is_expensive, prices)))   # [120, 300]
print(list(filter(is_mid_range, prices)))   # [80, 60]
