import requests
import os
from PIL import Image
from grab import Grab
from pyquery import PyQuery as pq

g = Grab()
resp = g.go('https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html')
resp.body

doc = pq(resp.body)
title = doc('title')
print(type(title), title.text())

# 決定要儲存的資料夾
output_dir = 'downloads'

# 假如資料夾不存在就新增一個資料夾
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 定位所有圖片的 tag
# image_tags = soup.find(id='main-content').findChildren('a', recursive=False)
image_tags = doc('#main-content a')
tag_name = image_tags.text()
print(tag_name)
for img_tag in image_tags:
    # 取得所有圖片在第三方服務的 id
    img_id = img_tag['href'].split('/')[-1]
    # 組合圖片而非網站的網址
    img_url = 'https://i.imgur.com/{}.jpg'.format(img_id)
    # 對圖片送出請求
    with requests.get(img_url, stream=True) as r:
        r.raise_for_status()
        # 檢查圖片副檔名
        img = Image.open(r.raw)
        img_savename = '{outdir}/{img_id}.{img_ext}'.format(
            outdir=output_dir, img_id=img_id, img_ext=img.format.lower())
        img.save(img_savename)
        print('Save image {}'.format(img_savename))