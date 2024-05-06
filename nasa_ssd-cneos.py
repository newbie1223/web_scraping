import requests
import json
from datetime import datetime

#NASAのAPIエンドポイント
url = "https://ssd-api.jpl.nasa.gov/scout.api"

#APIキーを設定します。あなたのAPIキーに置き換えてください。
# api_key = "WqJ7vCloQkrQeMQ33MxTvBrD0j0qcmigTktwg3i1"

#現在の日時を取得します。
current_time = datetime.now().isoformat()

#パラメータを設定します。
params = {
    # "api_key": api_key,
    # "-h":"Ceres",
    # "-t":current_time,
}

#APIリクエストを送信します。
response = requests.get(url, params=params)

#レスポンスをJSON形式で取得します。
data = response.json()

#天体の名前と軌道情報を表示します。
# for body in data['bodies']:
#     print(f"天体の名前: {body['ObjectName']}")
#     print(f"軌道情報: {body['orbits']}")
print(json.dumps(data, indent=4))
# print(f"天体の名前: {data['objectName']}")
# print(f"軌道情報: {data['orbits']}")