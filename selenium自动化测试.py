from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Chrome()

url=' '
driver.get(url)

driver.find_element_by_xpath('  ').send_keys('input what you want to')   #向输入框输入字符
driver.find_element_by_xpath('  ').click()                               #点击
driver.find_element_by_xpath('  ').clear()                               #清除框内信息

soup=Beautiful(driver.page_source,'lxml')                                #driver.page_source 即为获取网页源代码，此处即解析源代码

iitems=soup.find_all('div','')                                           #接下来就是正常的用 BeautifulSoup 进行解码了
for item in items:
  ......


# 之后详细去看一下官方文档之后再来补充（2017/9/23）
