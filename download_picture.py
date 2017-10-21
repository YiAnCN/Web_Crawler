import requests
import os
import urllib.request

from bs4 import BeautifulSoup



def get_url(url):
    try:
        r=requests.get(url)
        # r.raise_for_status()
        return r.text
    except:
        print(404)

def parse_page(html):
    count=0
    # path = os.getcwd() + '/tupian/' + str(count) + '.jpg'
    soup=BeautifulSoup(html,'lxml')
    divss=soup.find_all('div','item')
    for divs in divss:
        try:
            div1=divs.find('img')
            div2=div1.get('src')
            div3=div1.get('data-lazy')
            div4=div3 if (len(div2) == 21) else div2
            urllib.request.urlretrieve(div4,os.getcwd() + '/tupian/' + str(count) + '.jpg')
            count += 1
        except:
            continue
        # with open (path , 'wb') as f:
        #     f.write(div4)

        # print(div4)

        # if len(div1)==21:
        #     print(divs.find('img').get('data-lazy'))

def main():
    url='https://pixabay.com/?gallery&media_type=photo'
    html=get_url(url)
    parse_page(html)

if __name__ == '__main__':
    # for page in range(1, ):
    main()
