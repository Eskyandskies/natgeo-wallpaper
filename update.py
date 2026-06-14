import requests
import re

url = "https://www.nationalgeographic.com/photography/photo-of-the-day/"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

html = requests.get(url, headers=headers).text

match = re.search(
    r'<meta property="og:image" content="([^"]+)"',
    html
)

if not match:
    raise Exception("Image not found")

img_url = match.group(1)

img = requests.get(img_url, headers=headers)

with open("latest.jpg", "wb") as f:
    f.write(img.content)

print("Updated")