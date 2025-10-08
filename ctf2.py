from web3 import Web3
from web3.exceptions import ContractLogicError
import json
import solcx
import time

# --- 1. Setup Connection and Addresses ---
print("--- 1. Setting up connection and loading addresses ---")
RPC_URL = "http://35.89.115.2220:8545"
privateKey = "aa70368a9bf27321784b9078ed1ac8a291700cdae2f712e29ed7aedff7ce6d9f"  
TARGET_CONTRACT_ADDRESS = Web3.to_checksum_address("0x3Eb1C5c2F67b94a82B0c59fAa52e750b812a8952")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    raise ConnectionError("Failed to connect to the RPC URL")

account = w3.eth.account.from_key(privateKey)
my_address = account.address
print(f"My address: {my_address}")
