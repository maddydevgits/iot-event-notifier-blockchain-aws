from web3 import Web3, HTTPProvider
from ca import *
import json
from time import sleep
from SendEmail import *

owneremail='parvathanenimadhu@gmail.com'

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

count=0
while True:
    contract,web3=connect_with_blockchain(0)
    p,w=contract.functions.viewFeed().call()
    l=len(p)
    if l>count:
        for i in range(count,l):
            if(p[i]<25):
                verifyIdentity(owneremail)
                while True:
                    try:
                        a=sendmessage('IoT Event Notification',p[i],w[i],owneremail)
                        if(a):
                            break
                        else:
                            continue
                    except:
                        sleep(10)

            payload='{"Pressure":'+str(p[i])+',"Wheel":'+str(w[i])+'}'
            print(payload)
            sleep(4)
        else:
            count=l
