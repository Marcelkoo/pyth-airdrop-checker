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
        print("Неверный выбор. Пожалуйста, выберите 1 для EVM или 2 для Solana.")
        return

    for address in addresses:
        response = requests.get(url + address)
        try:
            data = response.json()
            if 'error' in data:
                print(f"Ошибка: {data['error']} для адреса {address}")
            else:
                print(f"Адрес: {address}, Данные: {json.dumps(data, indent=2)}")
        except json.JSONDecodeError:
            print(f"Не удалось обработать ответ для адреса {address}")

def main():
    choice = int(input("Введите 1 для проверки EVM кошельков, 2 для проверки Solana кошельков: "))
    check_wallets(choice)

if __name__ == "__main__":
    main()
