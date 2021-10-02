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

factory_address = web3.toChecksumAddress(exchange["Pancakeswap"]["factory"])
contract        = web3.eth.contract(address=factory_address, abi=exchange["Pancakeswap"]["factory_abi"])
pair_address    = contract.functions.getPair( web3.toChecksumAddress(token["BUSD"]), web3.toChecksumAddress(token["ETH"])).call()
pair1           = web3.eth.contract(abi=exchange["Pancakeswap"]["pair_abi"], address=pair_address)
reserves = pair1.functions.getReserves().call()
reserve0 = reserves[0]
reserve1 = reserves[1]

print(f'{reserve1/reserve0}')

contract    = web3.eth.contract(address=web3.toChecksumAddress(web3.toChecksumAddress(token["ETH"])), abi=exchange["Pancakeswap"]["pair_abi"])
address     = web3.toChecksumAddress(wallet)
balance     = web3.fromWei(contract.functions.balanceOf(address).call(), "ether")

print(f'{float(balance * reserve1/reserve0):.2f}')