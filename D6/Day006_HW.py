#  -*- coding: utf-8 -*-
# 取出知乎問題發問時間
# 取出第一筆與最後一筆回答的時間

import requests
import json
import time
headers = {
    # 'Accept':'text/html,application/xhtml+xm…ml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Language':	'zh-TW,en;q=0.9,ja;q=0.8,id;q=0…DE;q=0.3,th;q=0.2,ko-KR;q=0.1',
    # 'Cache-Control'	:'max-age=0',
    # 'Connection':'keep-alive',	
    # 'DNT':	'1',
    # 'Host':	'www.zhihu.com',
    # 'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 Firefox/73.0'
}
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers = headers)
response = json.loads(r.text)
question_time = response['data'][0]['question']['created']
timeArray = time.localtime(question_time)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
otherStyleTime
answer_time_list = []
for answer_data in response['data']:
    answer_time = answer_data['created_time']
    answer_time_list.append(answer_time)
first_answer_time = answer_time_list[0]
timeArray = time.localtime(first_answer_time)
first_answer_time_format = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
last_answer_time = answer_time_list[len(response['data'])-1]
timeArray = time.localtime(last_answer_time)
last_answer_time_format = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(first_answer_time_format)
print(last_answer_time_format)

