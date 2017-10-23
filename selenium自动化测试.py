from selenium import webdriver
from selenium.webdriver.common.keys import Keys                          # `Keys`类提供键盘按键的支持，比如：RETURN, F1, ALT等

from bs4 import BeautifulSoup

driver=webdriver.Chrome()                                                # 创建一个Chrome WebDriver的实例

url=' '                                                                  # driver.get 方法将打开URL中填写的地址，WebDriver 将等待， 直到页面完全加载完毕
driver.get(url)                                                          # 值得注意的是，如果你的页面使用了大量的Ajax加载， WebDriver可能不知道什么时候页面已经完全加载

elem = driver.find_element_by_name("q")                                  # 找到输入框
elem.clear()                                                             # 清除input输入框中的任何预填充的文本
elem.send_keys('input that you what to write ')                          # 向输入框输入你想要输入的字符.
elem.send_keys(Keys.RETURN)                                              # 相当于键盘按下 RETURN 键




driver.find_element_by_xpath('  ').send_keys('input that you want to write')   # 向输入框输入字符
driver.find_element_by_xpath('  ').click()                               # 点击
driver.find_element_by_xpath('  ').clear()                               # 清除框内信息

soup=Beautiful(driver.page_source,'lxml')                                # driver.page_source 即为获取网页源代码，此处即解析源代码

iitems=soup.find_all('div','')                                           # 接下来就是正常的用 BeautifulSoup 进行解码了
for item in items:
  ......


# 显式等待

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
    
    
    
    
# 模拟点击用  element_to_be_clickable

from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))



# 判断某个给定的文本是否存在于指定的元素中
用                   EC.text_to_be_present_in_element


    
    
   
