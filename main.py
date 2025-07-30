import tkinter as tk
import requests
from tkinter import font as tkFont

root = tk.Tk()
root.title("Currency & Crypto Converter")
root.geometry("500x360")
BG_DARK = "#2C3E50"
BG_LIGHT = "#34495E"
FG_LIGHT = "#ECF0F1"
ACCENT_COLOR = "#2980B9"
RESULT_COLOR = "#F1C40F"

root.configure(bg=BG_DARK)

result_var = tk.StringVar()

title_font = tkFont.Font(family="Segoe UI", size=24, weight="bold")
label_font = tkFont.Font(family="Segoe UI", size=11, weight="bold")
button_font = tkFont.Font(family="Segoe UI", size=11, weight="bold")
entry_font = tkFont.Font(family="Segoe UI", size=10)
result_font = tkFont.Font(family="Segoe UI", size=15, weight="bold")

currency_list = [
    "USD", "EUR", "INR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY",
    "NZD", "SGD", "HKD", "SEK", "KRW", "ZAR", "MXN", "BRL", "TRY",
    "RUB", "PLN", "THB", "IDR", "PHP", "SAR", "AED", "EGP", "NOK",
    "DKK", "HUF", "ILS", "TWD", "UAH", "VND"
]
crypto_list = [
    "BTC", "ETH", "BNB", "SOL", "XRP", "ADA", "DOGE", "SHIB", "AVAX",
    "DOT", "LINK", "LTC", "TRX", "MATIC", "UNI", "BCH", "XLM", "ICP",
    "FIL", "APT", "IMX", "NEAR", "ETC", "ATOM", "XMR", "HBAR", "VET",
    "QNT", "GRT", "AAVE", "MKR", "EOS", "ALGO", "SAND", "MANA", "AXS",
    "FTM", "PEPE", "WIF"
]

tk.Label(root, text="Currency & Crypto Converter", font=title_font, bg=BG_DARK, fg=FG_LIGHT).grid(row=0, column=0, columnspan=2, pady=(15, 10), sticky="ew")

currency_frame = tk.LabelFrame(root, text="Fiat Currency Conversion", font=label_font, bg=BG_LIGHT, fg=FG_LIGHT, padx=15, pady=10, relief="groove", bd=3)
currency_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

from_currency_var = tk.StringVar(value=currency_list[0])
to_currency_var = tk.StringVar(value=currency_list[2])

tk.Label(currency_frame, text="From:", bg=BG_LIGHT, fg=FG_LIGHT, font=label_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.OptionMenu(currency_frame, from_currency_var, *currency_list).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
tk.Label(currency_frame, text="To:", bg=BG_LIGHT, fg=FG_LIGHT, font=label_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.OptionMenu(currency_frame, to_currency_var, *currency_list).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

amount_var = tk.StringVar(value="1.0")
tk.Label(currency_frame, text="Amount:", bg=BG_LIGHT, fg=FG_LIGHT, font=label_font).grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Entry(currency_frame, textvariable=amount_var, width=15, font=entry_font,
         bg=FG_LIGHT, fg=BG_DARK, insertbackground=BG_DARK, relief="sunken", bd=2).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

def convert_currency():
    from_cur = from_currency_var.get()
    to_cur = to_currency_var.get()
    try:
        amount = float(amount_var.get())
    except ValueError:
        result_var.set("Invalid amount. Enter a number.")
        return

    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        rate = data['rates'].get(to_cur)
        if rate:
            converted = amount * rate
            result_var.set(f"{amount:.2f} {from_cur} = {converted:.4f} {to_cur}")
        else:
            result_var.set(f"Could not find rate for {to_cur}.")
    except requests.exceptions.Timeout:
        result_var.set("Request timed out. Try again.")
    except requests.exceptions.ConnectionError:
        result_var.set("Network error. Check your internet connection.")
    except requests.exceptions.HTTPError:
        result_var.set("HTTP Error occurred.")
    except Exception as e:
        result_var.set(f"Error fetching rates: {e}")

crypto_frame = tk.LabelFrame(root, text="Crypto Conversion", font=label_font, bg=BG_LIGHT, fg=FG_LIGHT, padx=15, pady=10, relief="groove", bd=3)
crypto_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

crypto_var = tk.StringVar(value=crypto_list[0])
crypto_to_var = tk.StringVar(value=currency_list[0])

tk.Label(crypto_frame, text="From:", bg=BG_LIGHT, fg=FG_LIGHT, font=label_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.OptionMenu(crypto_frame, crypto_var, *crypto_list).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
tk.Label(crypto_frame, text="To:", bg=BG_LIGHT, fg=FG_LIGHT, font=label_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.OptionMenu(crypto_frame, crypto_to_var, *currency_list).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

crypto_amount_var = tk.StringVar(value="1.0")
tk.Label(crypto_frame, text="Amount:", bg=BG_LIGHT, fg=FG_LIGHT, font=label_font).grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Entry(crypto_frame, textvariable=crypto_amount_var, width=15, font=entry_font,
         bg=FG_LIGHT, fg=BG_DARK, insertbackground=BG_DARK, relief="sunken", bd=2).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

def convert_crypto():
    symbol = crypto_var.get()
    convert_to = crypto_to_var.get()
    try:
        amount = float(crypto_amount_var.get())
    except ValueError:
        result_var.set("Invalid amount. Enter a number.")
        return

    api_key_cmc = '6da3963e-b2ae-4f2e-92aa-d1f6ab178945'
    url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
    params = {'amount': amount, 'symbol': symbol, 'convert': convert_to}
    headers = {'X-CMC_PRO_API_KEY': api_key_cmc}

    try:
        r = requests.get(url, params=params, headers=headers)
        data = r.json()
        if 'data' in data and data['data'] and 'quote' in data['data'][0] and convert_to in data['data'][0]['quote']:
            price = data['data'][0]['quote'][convert_to]['price']
            result_var.set(f"{amount:.4f} {symbol} = {price:.2f} {convert_to}")
        else:
            result_var.set("Error")
    except Exception:
        result_var.set("Error")

tk.Button(currency_frame, text="Convert", command=convert_currency, bg=ACCENT_COLOR, fg=FG_LIGHT, font=button_font, relief="raised", bd=3, padx=10, pady=5).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
tk.Button(crypto_frame, text="Convert", command=convert_crypto,
          bg=ACCENT_COLOR, fg=FG_LIGHT, font=button_font,
          relief="raised", bd=3, padx=10, pady=5).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

tk.Label(root, textvariable=result_var, bg=BG_DARK, fg=RESULT_COLOR, font=result_font,
         wraplength=480, justify="center").grid(row=2, column=0, columnspan=2, pady=(10, 20), sticky="ew")

currency_frame.grid_columnconfigure(1, weight=1)
crypto_frame.grid_columnconfigure(1, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)

root.mainloop()
