
import requests
import json
# from googletrans import Translator

#NASAのAPIエンドポイント
url = "https://api.nasa.gov/planetary/apod"

#APIキーを設定します。あなたのAPIキーに置き換えてください。
api_key = "WqJ7vCloQkrQeMQ33MxTvBrD0j0qcmigTktwg3i1"

#パラメータを設定します。
params = {
    "api_key": api_key,
}

#APIリクエストを送信します。
response = requests.get(url, params=params)

#レスポンスをJSON形式で取得します。
data = response.json()

#Google翻訳APIを初期化します。
# translator = Translator()

#天体の説明を日本語に翻訳します。
# translated_explanation = translator.translate(data['explanation'], dest='ja')

#天体の写真とその説明を表示します。
print(f"Title: {data['title']}")
print(f"URL: {data['url']}")
# print(f"Explanation (Japanese): {translated_explanation.text}")
print(f"Explanation: {data['explanation']}")