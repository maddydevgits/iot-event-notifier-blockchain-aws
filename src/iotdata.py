import random
from web3 import Web3, HTTPProvider
from ca import *
import json
from time import sleep

def iotSensoryFeed():
    pressure=random.randint(20,100)
    wheelNo=random.randint(1,4)
    return (pressure,wheelNo)

def connect_with_blockchain(acc):
    web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
    if(acc==0):
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc
    compiled_contract_path='../build/contracts/iot.json'
    deployed_contract_address=iotContractAddress

    with open(compiled_contract_path) as file:
        contract_json=json.load(file)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=deployed_contract_address,abi=contract_abi)
    return contract, web3

while True:
    p,w=iotSensoryFeed()
    contract,web3=connect_with_blockchain(0)
    tx_hash=contract.functions.addFeed(p,w).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    sleep(4)
    print('Block Added')