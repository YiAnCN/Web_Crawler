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
        # for item in Data['data']:
        #     yield item['article_url']
    # return Data.get('data')

        if Data and 'data' in Data.keys():
            for item in Data.get('data'):
                yield item.get('article_url')
    except:
        pass
    # htmldict=Data['data']
    # yield htmldict.get('article_url')


    # return htmldict

def main():
    url='https://www.toutiao.com/search_content/'
    html=get_page(url)
    for url in parse_page(html):
        print(url)
    # print(parse_page(html))

if __name__ == '__main__':
    main()

