import requests

api = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = requests.get(api, headers=headers).json()

img_url = "https://www.bing.com" + data["images"][0]["url"]

img = requests.get(img_url, headers=headers)

with open("latest.jpg", "wb") as f:
    f.write(img.content)

print("OK:", img_url)