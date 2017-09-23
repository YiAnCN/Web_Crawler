from selenium import webdriver

driver=webdriver.Chrome()

url=' '
driver.get(url)

driver.find_element_by_xpath('  ').send_keys('input what you want to')   #向输入框输入字符
driver.find_element_by_xpath('  ').click()                               #点击

