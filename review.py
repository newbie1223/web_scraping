import requests
from bs4 import BeautifulSoup
# import urllib.request as req
# import pandas as pd
# from selenium import webdriver
# import chromedriver_binary
# import datetime
# from datetime import date
# from datetime import timedelta
# import time

# #google chromeを起動
# browser = webdriver.Chrome()
# #chrome find waite
# browser.implicitly_wait(3)

# #page access
urlName = "https://shareview.jp/item/detail/694"
# # url go
# browser.get(urlName)
# #トップページのURL
# # urlName = "https://minbeer.com/beer-ranking"

# #ページが開くまで待機
# time.sleep(3)

# x = 1
# while x <= 20:
#     #click next page
#     browser_from = browser.find_element_by_class_name("more btn-more js-moreReview")
#     time.sleep(3)
#     browser_from.click()
#     print('click')
#     x += 1

# time.sleep(3)
# #ページのHTMLを取得
# response = req.urlopen(urlName)
# url = BeautifulSoup(response, 'html.parser')

#Requestsを使用してURLからデータを取得
url = requests.get(urlName)

#BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(url.content, 'html.parser')
# print(soup)

#特定のクラスを持つすべての要素を検索
reviews = soup.find_all("p")

#各トレンド記事トルを表示
for review in reviews:
    print(review.text)