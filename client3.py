import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote["stock"]
    bid_price = float(quote["top_bid"]["price"])
    ask_price = float(quote["top_ask"]["price"])
    price = (bid_price + ask_price) / 2  # Corrected price calculation
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """Get ratio of price_a and price_b"""
    if price_b == 0:  # Avoid division by zero
        return
    return price_a / price_b  # Corrected ratio calculation


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(
            urllib.request.urlopen(QUERY.format(random.random())).read()
        )

        prices = {}  # Dictionary to store stock prices

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store the price in the dictionary
            print(
                "Quoted %s at (bid:%s, ask:%s, price:%s)"
                % (stock, bid_price, ask_price, price)
            )

        # Assuming the quotes are for stock A and B
        if "A" in prices and "B" in prices:
            print(
                "Ratio %s" % getRatio(prices["A"], prices["B"])
            )  # Corrected ratio calculation
