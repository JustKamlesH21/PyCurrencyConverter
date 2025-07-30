<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency & Crypto Converter README</title>
    <!--
        NOTE: The <style> block below will NOT be rendered by GitHub's README.md.
        GitHub READMEs use Markdown and their own default styling.
        This HTML structure is provided if you intend to render it as a standalone HTML page.
    -->
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }
        h1 span {
            margin-right: 10px;
            font-size: 1.2em;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }
        p {
            margin-bottom: 10px;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
            margin-bottom: 10px;
        }
        ul.inline-list {
            list-style-type: none;
            padding: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
        }
        ul.inline-list li {
            background-color: #e0f2f7;
            padding: 5px 10px;
            border-radius: 4px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.9em;
            color: #0056b3;
        }
        pre {
            background-color: #ecf0f1;
            border: 1px solid #ddd;
            border-left: 4px solid #3498db;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin-bottom: 15px;
        }
        code {
            font-family: 'Consolas', 'Courier New', monospace;
            background-color: #e9ecef;
            padding: 2px 4px;
            border-radius: 3px;
            color: #c7254e;
        }
        pre code {
            background-color: transparent;
            padding: 0;
            color: #333;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        strong {
            color: #2c3e50;
        }
    </style>
</head>
<body>

    <h1><span role="img" aria-label="currency">💱</span> Currency & Crypto Converter <span role="img" aria-label="rocket">🚀</span></h1>

    <p>Welcome to the <strong>Currency & Crypto Converter</strong> project! This is a sleek and efficient desktop application built with Python and Tkinter, designed to provide real-time exchange rates for a wide array of global fiat currencies and popular cryptocurrencies.</p>

    <p>The magic happens by connecting to powerful online APIs that constantly update their exchange rates, ensuring you get the most current conversion values. No more outdated information – just instant, accurate results!</p>

    <h2><span role="img" aria-label="star">🌟</span> Features</h2>
    <ul>
        <li><strong>Dual Conversion Modes:</strong> Convert between fiat currencies or from cryptocurrency to fiat currency.</li>
        <li><strong>Real-time Rates:</b> Fetches live exchange rates from reliable APIs.</li>
        <li><strong>Wide Range of Currencies:</strong> Supports an extensive list of global fiat currencies and top cryptocurrencies.</li>
        <li><strong>User-Friendly Interface:</strong> A clean, modern, and intuitive graphical user interface (GUI) built with Tkinter.</li>
        <li><strong>Error Handling:</strong> Provides clear messages for network issues, invalid inputs, or API errors.</li>
    </ul>

    <h2><span role="img" aria-label="tools">🛠️</span> How It Works (Under the Hood)</h2>
    <p>The application leverages the power of external APIs to retrieve up-to-date exchange rates:</p>
    <ul>
        <li><strong>For Fiat Currency Conversions:</strong> Rates are fetched from the <a href="https://www.exchangerate-api.com/">ExchangeRate-API</a> (<code>v6</code> endpoint).</li>
        <li><strong>For Cryptocurrency to Fiat Conversions:</strong> Prices are obtained from the <a href="https://coinmarketcap.com/api/">CoinMarketCap Pro API</a> (<code>v2/tools/price-conversion</code> endpoint).</li>
    </ul>
    <p><strong>Important:</strong> Both APIs require an API key for usage. You will need to obtain your own keys and insert them into the code as instructed in the "Getting Started" section.</p>

    <h2><span role="img" aria-label="money bag">💰</span> Supported Currencies & Cryptocurrencies</h2>

    <h3>Fiat Currencies <span role="img" aria-label="earth">🌍</span></h3>
    <p>This converter supports a comprehensive list of world currencies, including but not limited to:</p>
    <ul class="inline-list">
        <li>USD</li><li>EUR</li><li>INR</li><li>GBP</li><li>JPY</li><li>AUD</li><li>CAD</li><li>CHF</li><li>CNY</li>
        <li>NZD</li><li>SGD</li><li>HKD</li><li>SEK</li><li>KRW</li><li>ZAR</li><li>MXN</li><li>BRL</li><li>TRY</li>
        <li>RUB</li><li>PLN</li><li>THB</li><li>IDR</li><li>PHP</li><li>SAR</li><li>AED</li><li>EGP</li><li>NOK</li>
        <li>DKK</li><li>HUF</li><li>ILS</li><li>TWD</li><li>UAH</li><li>VND</li>
    </ul>

    <h3>Cryptocurrencies <span role="img" aria-label="diamond">💎</span></h3>
    <p>Stay updated on the value of popular digital assets with support for:</p>
    <ul class="inline-list">
        <li>BTC</li><li>ETH</li><li>BNB</li><li>SOL</li><li>XRP</li><li>ADA</li><li>DOGE</li><li>SHIB</li><li>AVAX</li>
        <li>DOT</li><li>LINK</li><li>LTC</li><li>TRX</li><li>MATIC</li><li>UNI</li><li>BCH</li><li>XLM</li><li>ICP</li>
        <li>FIL</li><li>APT</li><li>IMX</li><li>NEAR</li><li>ETC</li><li>ATOM</li><li>XMR</li><li>HBAR</li><li>VET</li>
        <li>QNT</li><li>GRT</li><li>AAVE</li><li>MKR</li><li>EOS</li><li>ALGO</li><li>SAND</li><li>MANA</li><li>AXS</li>
        <li>FTM</li><li>PEPE</li><li>WIF</li>
    </ul>

    <h2><span role="img" aria-label="rocket">🚀</span> Getting Started</h2>
    <p>Follow these steps to set up and run the Currency & Crypto Converter on your local machine.</p>

    <h3>Prerequisites</h3>
    <p>Make sure you have Python installed on your system (Python 3.x recommended).</p>

    <h3>Installation</h3>
    <p>1. <strong>Clone the Repository:</strong></p>
    <pre><code>git clone https://github.com/YOUR_GITHUB_USERNAME/Currency-Crypto-Converter-Tkinter.git
cd Currency-Crypto-Converter-Tkinter</code></pre>
    <p><em>(Replace <code>YOUR_GITHUB_USERNAME</code> with your actual GitHub username and adjust the repository name if you chose a different one.)</em></p>

    <p>2. <strong>Install Dependencies:</strong><br>
    This project requires the <code>requests</code> library to make API calls.</p>
    <pre><code>pip install requests</code></pre>

    <h3>Obtaining API Keys (Crucial!)</h3>
    <p>For the converter to function, you need valid API keys:</p>
    <p>1. <strong>ExchangeRate-API (Fiat):</strong></p>
    <ul>
        <li>Go to <a href="https://www.exchangerate-api.com/">exchangerate-api.com</a></li>
        <li>Sign up for a free API key.</li>
        <li>Locate the line <code>api_key_exchangerate = 'YOUR_EXCHANGERATE_API_KEY'</code> in the <code>convert_currency</code> function in <code>main.py</code> (or your equivalent file).</li>
        <li>Replace <code>'YOUR_EXCHANGERATE_API_KEY'</code> with the key you obtained.</li>
    </ul>
    <p>2. <strong>CoinMarketCap Pro API (Crypto):</strong></p>
    <ul>
        <li>Go to <a href="https://coinmarketcap.com/api/">coinmarketcap.com/api/</a></li>
        <li>Sign up for a free developer account to get your API key. (Note: Free tier has usage limits.)</li>
        <li>Locate the line <code>api_key_cmc = 'YOUR_COINMARKETCAP_API_KEY'</code> in the <code>convert_crypto</code> function.</li>
        <li>Replace <code>'YOUR_COINMARKETCAP_API_KEY'</code> with your CoinMarketCap API key.</li>
    </ul>

    <h3>Running the Application</h3>
    <p>After installing dependencies and adding your API keys, run the main Python script:</p>
    <pre><code>python your_main_script_name.py  # e.g., python main.py</code></pre>
    <p>The converter GUI window should appear!</p>

    <h2><span role="img" aria-label="camera">📸</span> Screenshots</h2>
    <p><em>(Consider adding screenshots of your application here to showcase its UI.)</em></p>

    <hr>

    <h2><span role="img" aria-label="handshake">🙏</span> Credits</h2>
    <ul>
        <li>Built with Python and Tkinter.</li>
        <li>Powered by <a href="https://www.exchangerate-api.com/">ExchangeRate-API</a> and <a href="https://coinmarketcap.com/api/">CoinMarketCap API</a>.</li>
    </ul>

    <hr>

    <h2><span role="img" aria-label="license">📄</span> License</h2>
    <p>This project is open-source and available under the <a href="LICENSE">MIT License</a>. <em>(It's a good idea to create a <code>LICENSE</code> file in your repo if you want to explicitly state the license).</em></p>

</body>
