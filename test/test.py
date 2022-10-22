from web3 import Web3, HTTPProvider
import json

web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path='../build/contracts/register.json'
deployed_contract_address='0x89aCB71960D952298de03dfBefAa72248A05a6CB'

with open(compiled_contract_path) as file:
    contract_json=json.load(file)
    contract_abi=contract_json['abi']

contract=web3.eth.contract(address=deployed_contract_address,abi=contract_abi)

tx_hash=contract.functions.addUser('7893015625'.encode('utf-8'),'madhu'.encode('utf-8'),'hyderabad'.encode('utf-8'),'0xF367d0653669067c9ACb3A07f3b653ED90231946').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print(tx_hash)

_phonenos,_names,_places,_wallets=contract.functions.viewUsers().call()
print(_phonenos,_names,_places,_wallets)