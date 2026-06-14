import requests

url = "https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.gallery.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=20)

if r.status_code != 200:
    raise Exception(f"API HTTP {r.status_code}")

data = r.json()

# 通常第一张就是当天
try:
    image_url = data["items"][0]["src"]
except Exception:
    raise Exception("JSON structure changed")

img = requests.get(image_url, headers=headers, timeout=20)

with open("latest.jpg", "wb") as f:
    f.write(img.content)

print("OK:", image_url)