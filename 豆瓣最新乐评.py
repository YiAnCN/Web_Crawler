#Beautifulsoup如何解析两个 for 循环得出的内容并将其一一对应

import requests
import json
import time
from bs4 import BeautifulSoup

url='https://music.douban.com/review/latest/'
r=requests.get(url)
html=r.text

#预设两个空的列表
list1=[]
list2=[]

soup=BeautifulSoup(html,'lxml')
divs=soup.find_all('div','short-content')
items=soup.find_all('h3','title')
for divss in divs:
    divl=divss.get_text().replace(' ','')
    list1.append(divl)
for item in items:
    item1=item.get_text()
    list2.append(item)            #将内容添加到空列表中

#重点：下面三行代码实现一一对应
for i in range(len(list1)):
    a=list1[i],list2[i]
    print(a)
