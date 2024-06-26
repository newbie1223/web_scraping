import requests
from bs4 import BeautifulSoup

#トップページのURL
urlName = "https://qiita.com/"

#Requestsを使用してURLからデータを取得
url = requests.get(urlName)

#BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(url.content, 'html.parser')
# print(soup)

#特定のクラスを持つすべての要素を検索
reviews = soup.find_all("p",class_="style-2vm86z")

#各トレンド記事トルを表示
for review in reviews:
    print(review.text)