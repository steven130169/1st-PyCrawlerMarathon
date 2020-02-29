## 作業目標

# * 請利用 API: https://www.dcard.tw/_api/forums/pet/posts?popular=true 回答下列問題：

# 1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？


import requests
import json
r = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=true')
response = json.loads(r.text)
len(response)
print(len(response))
# 30個

# 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
count_num = 0
likeCount_num = 0
for response_content in response:
    title = response_content['title']
    time = response_content['createdAt']
    count = response_content['commentCount']
    count_num+=count
    likeCount = response_content['likeCount']
    likeCount_num+=likeCount

# 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
notPopular = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=false')
notPopular_response = json.loads(notPopular.text)
notPopular_count_num = 0
notPopular_likeCount_num = 0
for notPopular_content in notPopular_response:
    count = notPopular_content['commentCount']
    notPopular_count_num += count
    likeCount = notPopular_content['likeCount']
    notPopular_likeCount_num += likeCount

not_popular_count_average = notPopular_count_num/len(notPopular_response)
print(not_popular_count_average)
not_popular_likeCount_average = notPopular_likeCount_num/len(notPopular_response)
print(not_popular_likeCount_average)
popular_count_average = count_num/len(response)
print(popular_count_average)
popular_likeCount_average = likeCount_num/len(response)
print(popular_likeCount_average)