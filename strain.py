import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def get_stock_price(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('fin-streamer', {'class': 'livePrice svelte-mgkamr'})
    if divs:
        price = float(divs[0].find('span').text)
    else:
        price = 0.0
    return price

# 複数の銘柄の株価を取得
symbols = ['AAPL', 'GOOGL', 'TSLA']
prices = {symbol: get_stock_price(symbol) for symbol in symbols}

# pandas DataFrameに変換
df = pd.DataFrame(prices, index=[0])

# ダッシュボードを作成
df.plot(kind='bar')
plt.title('Stock Prices on ' + datetime.now().strftime('%Y-%m-%d'))
plt.xlabel('Companies')
plt.ylabel('Price')
plt.show()