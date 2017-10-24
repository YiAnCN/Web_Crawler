from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
# from bs4 import BeautifulSoup
import re
from pyquery import PyQuery as pq
import pymongo

client = pymongo.MongoClient(MONGO_URL, 27017)
db = client[MONGO_DB]
# meishi = db[MONGO_TABLE]

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def search():
    # try:
    url = 'https://www.taobao.com/'
    driver.get(url)

    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
    )
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
    )
    input.clear()
    input.send_keys(INPUT)
    submit.click()
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))
    )
    parse_page()
    return total.text
    # except TimeoutException:
    #     return search()


def change_page(page_number):
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
    )
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
    )
    input.clear()
    input.send_keys(page_number)
    submit.click()
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number))
    )
    parse_page()


def parse_page():
    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # divs = soup.find('div', 'items').find_all('div', 'item J_MouserOnverReq')
    # for divss in divs:
    #     div1 = divss.find('a').attr('alt')
    #     print(div1)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item.J_MouserOnverReq')))
    html = driver.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item.J_MouserOnverReq  ').items()
    for item in items:
        product = {
            'image': 'http:' + item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.J_ClickStat').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('Successfully Saved to Mongo', result)
            return True
        return False
    except Exception:
        print('存储到mongodb失败', result)


def main():
    total = search()
    items = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, items + 1):
        change_page(i)

        # print(total)


if __name__ == '__main__':
    main()
