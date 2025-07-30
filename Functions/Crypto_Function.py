import requests

def convert_crypto():
    symbol = input("Enter crypto symbol (e.g., BTC): ").strip().upper()
    convert_to = input("Enter target currency (e.g., USD): ").strip().upper()
    amount = 1  # Always use 1 coin

    api_key = '6da3963e-b2ae-4f2e-92aa-d1f6ab178945'
    url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
    params = {'amount': amount, 'symbol': symbol, 'convert': convert_to}
    headers = {'X-CMC_PRO_API_KEY': api_key}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        price = data['data'][0]['quote'][convert_to]['price']
        print(f"1 {symbol} = {price:.2f} {convert_to}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    convert_crypto()
