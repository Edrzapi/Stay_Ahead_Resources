prices = [25, 80, 120, 15, 300, 60]


# HOF with function condition (return true/false)
def filter_prices(prices, condition):
    result = []
    for price in prices:
        if condition(price):
            result.append(price)
    return result


def get_expensive_prices(price):
    return price >= 100

def get_cheap_prices(price):
    return price < 50

def get_mid_range_prices(price):
    return 50 <= price < 100

print(filter_prices(prices, lambda price: price % 2 != 0 and get_mid_range_prices(price)))


