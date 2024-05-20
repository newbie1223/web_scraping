import os
import requests
import base64
import io
from bs4 import BeautifulSoup
from PIL import Image



def downloadimages(keyword, num_images):
    url = "https://www.google.com/search?q=" + keyword
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/2.3',
    }

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making a request to the url: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')

    if not os.path.exists('images'):
        os.makedirs('images')

    for i, img in enumerate(images[:num_images]):
        try:
            img_url = img['src']
            response = requests.get(img_url)
            base64_img = base64.b64encode(response.content)
            # img = Image.open(BytesIO(response.content))
            img = Image.open(io.BytesIO(base64_img))
            img.save(os.path.join('images', f'{keyword}{i}.png'))
            img.show()
        except Exception as e:
            print(f"Could not download image {i}: {e}")

#使用例
# downloadimages('橋本環奈', 3)

base64_str = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='

# 文字列のカンマより前の部分を削除
# image_data = base64_str.split(',')[1]

# base64文字列をデコード
decoded_image = base64.b64decode(base64_str)

# BytesIOオブジェクトを作成し、デコードされた画像データを読み込む
image = Image.open(io.BytesIO(decoded_image))

# 画像をファイルに保存
image.save('image.png')