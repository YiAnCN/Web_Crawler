import requests
import json


def get_page(url):
    params = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'format': 'json',
        'keyword': '街拍',
        'offset': 0,
    }
    r=requests.get(url,params=params)
    return r.text

def parse_page(html):
    try:
        Data=json.loads(html)
        if Data and 'data' in Data.keys():    #用于判断'data'是否在Data这个字典中，也可以写成 if 'data' in Data.keys():
            #---------------------------------
            for item in Data.get('data'):
                yield item.get('article_url')
            #--------------------------------
            for item in Data['data']:
                yield item['article_url']
            #-------------------------------
            #两种写法均可以
    except:
        pass
    # htmldict=Data['data']
    # for item in htmldict:
        # yield item.get('article_url')

def main():
    url='https://www.toutiao.com/search_content/'
    html=get_page(url)
    for url in parse_page(html):
        print(url)
    # print(parse_page(html))

if __name__ == '__main__':
    main()

