prices = [25, 80, 120, 15, 300, 60]


def get_expensive_prices(prices):
    result = []

    for price in prices:
        if price >= 100:
            result.append(price)

    return result


def get_cheap_prices(prices):
    result = []

    for price in prices:
        if price < 50:
            result.append(price)

    return result


def get_mid_range_prices(prices):
    result = []

    for price in prices:
        if 50 <= price < 100:
            result.append(price)

    return result


print(get_expensive_prices(prices))
print(get_cheap_prices(prices))
print(get_mid_range_prices(prices))