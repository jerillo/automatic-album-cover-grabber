import json
import urllib.request
import os

with open('./top-songs.json') as f:
    data = json.load(f)

for item in data.get("items"):
    img_url = item.get("album").get("images")[0].get("url")
    print(img_url)
    filename = item.get("album").get("name") + '.jpeg'
    print(filename)
    fullfilename = os.path.join('./album_covers', filename)
    urllib.request.urlretrieve(img_url, fullfilename)
