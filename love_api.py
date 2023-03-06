# -*- coding:utf-8 -*-
# @project: 闲聊机器人 
# @filename:love_api.py
# @author: ShuleHao
# @contact: 2571540718@qq.com
# @time:2022/9/12
# @Blog:https://blog.csdn.net/hubuhgyf?type=blog
from bs4 import BeautifulSoup
import requests
import requests
import re
import http.client, urllib
import datetime
import json
# 定义发送一句土味情话的方法
def romantic():
    response = requests.get("https://api.lovelive.tools/api/SweetNothings")
    texts = response.text
    # 分割语句形成两句话
    qa = re.split("？|，", texts, 1)
    return qa
#恋爱宝典api
def love_talk(text):
    url = 'http://app.lihsk.com/lihsk/android/paster/getPasterByTitle.html'
    data = {
            'name':text ,
            'pageNumber': '1',
            'pageSize': '10'
        }
    html = requests.post(url=url, data=data).json()
    result=[]
    for i in html["list"]:
        result.append(i["content"])
    Reply=""
    for j in result:
        if len(j)>40:
            continue
        else:
            Reply=j
            break
    if Reply:
        if "男："in Reply:
            Reply=Reply[2:]
        elif "女："in Reply:
            Reply=Reply[2:]
        return Reply
    else:
        return None
def good_morning():
    conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode({'key': 'aa5800dbb81752bf0d5aeb0841e60103'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/zaoan/index', params, headers)
    res = conn.getresponse()
    data = res.read()
    json_result = json.loads(data.decode('utf8'))['newslist'][0]["content"]
    result="xxx，早上好呀，今天是我们在一起的第"+time_subtraction()+"天，xxxxxxx："+json_result#自己编
    return result
def good_night():
    conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode({'key': 'aa5800dbb81752bf0d5aeb0841e60103'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/wanan/index', params, headers)
    res = conn.getresponse()
    data = res.read()
    json_result = json.loads(data.decode('utf8'))['newslist'][0]["content"]
    result = "xxxxxx" + json_result+"xxxxxx"
    return result
def star():
    conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode({'key': 'aa5800dbb81752bf0d5aeb0841e60103', 'astro': 'scorpio'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/star/index', params, headers)
    res = conn.getresponse()
    data = res.read()
    json_result=json.loads(data.decode('utf8'))['newslist']
    result="xxxxxx星座运势请查收："
    for i in json_result:
        result+=i['type']
        result+="："
        result += i['content']
        result += "，"
    return result
def brain_teaser():
    conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode({'key': 'aa5800dbb81752bf0d5aeb0841e60103', 'num': '10'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/naowan/index', params, headers)
    res = conn.getresponse()
    data = res.read()
    json_result = json.loads(data.decode('utf8'))['newslist'][0]
    result="xxxxx答案是"+json_result["result"]
    quest="xxxxx"+json_result["quest"]+"xxxxx"
    return quest,result

def time_subtraction():
    love_data = datetime.datetime.strptime("20211116", "%Y%m%d")
    cur = datetime.datetime.now()
    result=str(abs(cur.now()-love_data)).split(",")[0][:-5]
    return result
