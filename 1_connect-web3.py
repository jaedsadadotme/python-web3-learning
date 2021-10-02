import json , os , requests
import json , os , requests
from web3   import Web3
from dotenv import load_dotenv

load_dotenv()
# -----------

wallet  = os.getenv('WALLET_ADDRESS')

network = "https://bsc-dataseed.binance.org/"
web3    = Web3(Web3.HTTPProvider(network))

print("-------------------------")
print(web3.isConnected() == True and "connected" or "error connecting")
print("-------------------------")