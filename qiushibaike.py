import requests
from bs4 import BeautifulSoup

def get_url(url):
    r=requests.get(url)
    r.raise_for_status()
    return r.text

def parse_for_page(html):
    list1=[]
    list2=[]
    soup=BeautifulSoup(html,'lxml')
    divs=soup.find_all('div','content')
    hh=soup.find_all('div','author clearfix')
    for div in divs:
        spans=div.find('span').get_text().strip()
        list1.append(spans)
    for h2 in hh:
        try:
            h22=h2.find_all('a')[1]
            h33=h22.find('h2').get_text().strip()
            list2.append(h33)
        except:
            continue
            
------------------------import----------------------
    for i,l in zip(list2,list1):
        print(i+'/'+l)
----------------------------------------------------

def main(page):
    url='https://www.qiushibaike.com/8hr/page/{}/'.format(page)
    html=get_url(url)
    parse_for_page(html)

if __name__ == '__main__':
    for page in range(14):
        main(page)
        
        
#没能实现作者和笑话一一对应，因为匿名用户无法爬出，不知何故。
