import requests
from bs4 import BeautifulSoup

url = "https://www.nationalgeographic.com/photography/photo-of-the-day/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=20)

if r.status_code != 200:
    raise Exception(f"HTTP {r.status_code}")

soup = BeautifulSoup(r.text, "html.parser")

img = soup.find("meta", property="og:image")

if not img:
    raise Exception("og:image not found")

img_url = img["content"]

img_data = requests.get(img_url, headers=headers, timeout=20)

with open("latest.jpg", "wb") as f:
    f.write(img_data.content)

print("Updated:", img_url)