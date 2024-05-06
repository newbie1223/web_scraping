import requests
from bs4 import BeautifulSoup

#QiitaのトップページのURL
url = "https://qiita.com/"

#Requestsを使用してURLからデータを取得
html = requests.get(url)

#BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html.text, 'html.parser')
# print(soup)

#特定のクラスを持つすべての要素を検索（ここではQiitaのトレンド記事のタイトルを取得）
trends = soup.find_all(class_="style-2vm86z")

#各トレンド記事トルを表示
for trend in trends:
    print(trend.text)