import requests
import json

def read_addresses(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_wallets(wallet_type):
    if wallet_type == 1:
        addresses = read_addresses('evm.txt')
        url = 'https://airdrop.pyth.network/api/grant/v1/evm_breakdown?identity='
    elif wallet_type == 2:
        addresses = read_addresses('solana.txt')
        url = 'https://airdrop.pyth.network/api/grant/v1/solana_breakdown?identity='
    else:
        print("Invalid choice. Please choose 1 for EVM or 2 for Solana.")
        return

    for address in addresses:
        response = requests.get(url + address)
        try:
            data = response.json()
            if 'error' in data:
                print(f"Error: {data['error']} for address {address}")
            else:
                print(f"Address: {address}, Data: {json.dumps(data, indent=2)}")
        except json.JSONDecodeError:
            print(f"Failed to process response for address {address}")

def main():
    choice = int(input("Enter 1 to check EVM wallets, 2 to check Solana wallets: "))
    check_wallets(choice)

if __name__ == "__main__":
    main()
