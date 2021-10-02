import json , os , requests
from web3   import Web3
from dotenv import load_dotenv

load_dotenv()

# ------
wallet  = os.environ.get('WALLET_ADDRESS')

network = "https://bsc-dataseed.binance.org/"
web3    = Web3(Web3.HTTPProvider(network))

print("-------------------------")
print(web3.isConnected() == True and "connected" or "error connecting")
print("-------------------------")
# ------------

with open('./contract/exchange.json', 'r') as fac_definition:
 exchange = json.load(fac_definition)
with open('./contract/token.json', 'r') as token_def:
 token = json.load(token_def)

token               = web3.toChecksumAddress(token["ETH"])
token_contract      = web3.eth.contract(address=web3.toChecksumAddress(token), abi=exchange["WardenSwap"]["abi"])

address             = web3.toChecksumAddress(wallet)
balance             = token_contract.functions.balanceOf(address).call()
spend_symbol        = token_contract.functions.symbol().call()
print("balance" ,balance)

humanReadable = web3.fromWei(balance,'ether')
print("human balance",humanReadable)