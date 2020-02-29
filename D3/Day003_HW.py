#  -*- coding: utf-8 -*-
import os
# print(os.getcwd())

# 1. 請問高雄市有多少地區有溫度資料？ 38個
import xmltodict
fh = open("./D3/data/64_Weekday_CH.xml", "r",encoding="utf-8")
xml = fh.read()
d = dict(xmltodict.parse(xml))
# print(d)
locationsName = d['cwbopendata']['dataset']['locations']['locationsName']
location_list = d['cwbopendata']['dataset']['locations']['location']
KaohsiungCount = len(location_list)

# fh.close()
# print(xml)
print(KaohsiungCount)

# 2. 請取出每一個地區所記錄的第一個時間點跟溫度
location_area_list = []
temperature_list = []
startTime_list = []
for location_item in location_list:
    location = location_item['locationName']
    location_area_list.append(location)
    location_wetherElement = location_item['weatherElement'][0]
    wetherElement_time = location_wetherElement['time'][0]
    temperature = wetherElement_time['elementValue']['value']
    temperature_list.append(temperature)
    startTime = wetherElement_time['startTime']
    startTime_list.append(startTime)
location_dict ={
    'location':location_area_list,
    'temperation':temperature_list,
    'startTime':startTime_list,
}
print(location_dict)


# 3. 請取出第一個地區所記錄的每一個時間點跟溫度
first_location_temperature_startTime_list = []
first_location_temperature_list = []
first_location = location_list[0]
first_location_wetherElement = first_location['weatherElement'][0]
first_location_wetherElement_time_list = first_location_wetherElement['time']
for first_location_wetherElement_time in first_location_wetherElement_time_list:
    first_location_wetherElement_time_startTime = first_location_wetherElement_time['startTime']
    first_location_temperature_startTime_list.append(first_location_wetherElement_time_startTime)
    first_location_temperature = first_location_wetherElement_time['elementValue']['value']
    first_location_temperature_list.append(first_location_temperature)
first_location_dict={
    'first_location_temperature_startTime':first_location_temperature_startTime_list,
    'first_location_temperature':first_location_temperature_list
}
print(first_location_dict)