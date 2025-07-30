import requests
def convert_currency():
    from_cur = input("Enter the currency you want to convert from (e.g., USD): ").strip().upper()
    to_cur = input("Enter the currency you want to convert to (e.g., EUR): ").strip().upper()
    amount = float(input("Enter the amount to convert: "))

    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        rate = data['rates'].get(to_cur)
        if rate:
            converted = amount * rate
            result_var=print(f"{amount:.2f} {from_cur} = {converted:.4f} {to_cur}")
        else:
            print(f"Could not find rate for {to_cur}.")

    except Exception as e:
        print(f"Error fetching rates: {e}")
convert_currency()