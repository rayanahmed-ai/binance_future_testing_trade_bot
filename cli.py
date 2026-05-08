
import argparse
from colorama import Fore, init

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import validate_order
from bot.logging_config import logger

# Initialize colorama
init(autoreset=True)



# Create parser
parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

# CLI arguments
parser.add_argument(
    "--symbol",
    required=True,
    help="Trading symbol (example: BTCUSDT)"
)

parser.add_argument(
    "--side",
    required=True,
    choices=["BUY", "SELL"],
    help="Order side"
)

parser.add_argument(
    "--type",
    required=True,
    choices=["MARKET", "LIMIT"],
    help="Order type"
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Price required for LIMIT orders"
)

# Parse CLI arguments
args = parser.parse_args()
# Connection message
print(Fore.CYAN + "Connecting to Binance Futures Testnet...")
try:

    logger.info("CLI started")

    # Validate input
    validate_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    logger.info(
        f"Order Request -> "
        f"Symbol={args.symbol}, "
        f"Side={args.side}, "
        f"Type={args.type}, "
        f"Quantity={args.quantity}, "
        f"Price={args.price}"
    )

    # Print order summary
    print(Fore.YELLOW + "\n========== ORDER SUMMARY ==========")
    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Type        : {args.type}")
    print(f"Quantity    : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price       : {args.price}")

    print(Fore.YELLOW + "==================================")

    # Place MARKET order
    if args.type == "MARKET":

        response = place_market_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity
        )

    # Place LIMIT order
    else:

        response = place_limit_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity,
            price=args.price
        )

    # logger.info(f"Order Response -> {response}")

    # Print response
    print(Fore.CYAN + "\n========== RESPONSE ==========")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
    print(Fore.CYAN + "================================")

    # Success message
    print(Fore.GREEN + "\n✓ Order placed successfully")

except Exception as e:

    logger.error(f"Error -> {str(e)}")

    # Error message
    print(Fore.RED + f"\nError: {e}")