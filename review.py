import requests
from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from datetime import date
from datetime import timedelta
import time
import csv

# Google Chromeを起動
browser = webdriver.Chrome()
# Chrome find wait
browser.implicitly_wait(10)

# ページにアクセス
urlName = "https://shareview.jp/item/detail/87"
browser.get(urlName)

x = 1
while x <= 15:
    try:
        # 要素が存在するまで待つ
        element = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="productsWrap"]/div[2]/div/div[2]/div/div[{x}1]/a/span'))
        )
        print("Element is found")
        # 要素がクリック可能になるまで待つ
        # element = WebDriverWait(browser, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div[11]/a/span'))
        # )
        # 要素が画面内に表示されるようにスクロール
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # スクロール後に待機時間を設ける
        # JavaScript Executorを使ってクリック
        browser.execute_script("arguments[0].click();", element)
        print('click')
        x += 1
    except Exception as e:
        print(f"An error occurred: {e}")
        break

time.sleep(3)
# ページのHTMLを取得
# response = req.urlopen(urlName)
url = BeautifulSoup(browser.page_source, 'html.parser')

# 特定のクラスを持つすべての要素を検索
reviews = url.find_all("p")

# 各トレンド記事を表示
# for review in reviews:
#     print(review.text)

with open('reviews.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([review.text for review in reviews])

df = pd.read_csv('./reviews/reviews.csv')
print(df)

browser.quit()
