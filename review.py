import requests
from bs4 import BeautifulSoup

#トップページのURL
urlName = "https://minbeer.com/beer-ranking"

#Requestsを使用してURLからデータを取得
url = requests.get(urlName)

#BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(url.content, 'html.parser')
# print(soup)

#特定のクラスを持つすべての要素を検索
reviews = soup.find_all("div",class_="toc-content")

#各トレンド記事トルを表示
for review in reviews:
    print(review.text)