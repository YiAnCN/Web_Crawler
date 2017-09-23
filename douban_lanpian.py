爬取豆瓣烂片top250

import requests
import time
from bs4 import BeautifulSoup

def get_page(url):
    r=requests.get(url)
    r.raise_for_status()
    return r.text

def parse_page(html):
    soup=BeautifulSoup(html,'lxml')
    divs=soup.find_all('div','pl2')
    for div1 in divs:
        try:
            div2=div1.find('a').get_text().replace(' ','')
            div3=div1.find('p').get_text()
            div4=div1.find('div').find_all('span')[1].get_text()
            div5 = div1.find('div').find_all('span')[2].get_text()
            with open(r'C:\Users\Williams_Z\Desktop\movie5.txt','a+',encoding='utf-8') as f:
                content=div2 + ';' + div3 + ';' + div4 +' '+'\\'+' '+ div5 +'\n'
                f.write(content)           # try 里面的写法框架需要理解掌握
        except:
            continue
    time.sleep(1)             # try,except 真的能解决很多debug

def main(page):
    url='https://movie.douban.com/tag/%E7%83%82%E7%89%87?start={}'.format(page)
    html=get_page(url)
    parse_page(html)

if __name__ == '__main__':
    for page in range(106):
        main(page*20)
    print('Good Job')
