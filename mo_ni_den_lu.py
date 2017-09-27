import requests
from bs4 import BeautifulSoup
import os, time
import re

agent ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}


#获取_xsrf(通过BeautifulSoup解析库解析）

session = requests.Session()
homeurl = 'https://www.zhihu.com'
homeresponse = session.get(url=homeurl, headers=headers)
homesoup = BeautifulSoup(homeresponse.text, 'html.parser')
xsrfinput = homesoup.find('input', {'name': '_xsrf'})
#取dict中的值
xsrf_token = xsrfinput['value'] 
print("获取到的xsrf_token为： ", xsrf_token)
