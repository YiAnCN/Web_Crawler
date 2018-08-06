import requests
from bs4 import BeautifulSoup



def get_html(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    r.raise_for_status()
    return r.text

def parse_page(html):
    soup = BeautifulSoup(html,'html.parser')
    news = soup.find('div','box-text-title')
    news_title = news.get_text()
    news_href = news.find('a').get('href')
    return "新闻标题："+news_title+"\n新闻地址："+news_href




