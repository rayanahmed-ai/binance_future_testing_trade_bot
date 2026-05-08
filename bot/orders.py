from bot.client import client


def place_market_order(symbol, side, quantity):

    response = client.new_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    return response


def place_limit_order(symbol, side, quantity, price):

    response = client.new_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    return response