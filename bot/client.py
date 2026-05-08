from dotenv import load_dotenv
from binance.um_futures import UMFutures
import os


load_dotenv()


api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")


client = UMFutures(
    key=api_key,
    secret=api_secret,
    base_url = "https://testnet.binancefuture.com"
)

print(client.ping())