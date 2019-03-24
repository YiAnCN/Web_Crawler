import requests
from bs4 import BeautifulSoup
import pymysql

headers = {'cookie': 'd_c0="ANBmQrzayg2PTszf32I33V3ihKTWivJQ8rI=|1529731630"; _zap=b0c32807-8dac-47ea-9451-5250f1f57735; __utma=51854390.15960199.1532888156.1532888156.1532888156.1; __utmv=51854390.100--|2=registration_date=20170723=1^3=entry_date=20170723=1; _xsrf=FUpowODpg6I5vVw4EriOATu4zCNEQcvo; capsion_ticket="2|1:0|10:1552720854|14:capsion_ticket|44:MTAwOWYwNTI1YzUzNGM1MzkwZDE2YmU3ZTNhMTc1MWY=|f36fa1493a0c119e8cf6ab2f68ae4c51554cca5e04e04d933f25f041228564c6"; z_c0="2|1:0|10:1552721049|4:z_c0|92:Mi4xbmdtQkJRQUFBQUFBMEdaQ3ZOcktEU2NBQUFDRUFsVk5tVEcwWEFCQ255eTNFQTBNbkJwbkxvZlFZd2hHSjRocXd3|dd716e255de1678c963525ecc47294f777ec4641f410e2f6d030f9c8d53fe9be"; q_c1=688576e365af4727ac152ba1bbbf7659|1553068750000|1529731630000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; tst=h',
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

db = pymysql.connect("localhost","root","admin","demo1" )
db_table = 'news'
cursor = db.cursor()

result = dict()
# result = []

def get_html(url):
    r = requests.get(url,headers = headers)
    r.encoding = 'utf8'
    r.raise_for_status()
    return r.text

def parse_page(html):
    soup=BeautifulSoup(html,'lxml')
    divss = soup.find('div', 'Topstory-hot HotList')
    for divs in divss:
        idss = divs.find_all('div','HotItem-rank')
        for ids in idss:
            id = ids.get_text()
            # print(id)
            result['id'] = id
            # result.append(id)
        div = divs.find_all('div','HotItem-content')
        for a in div:
            a1 = a.find('a')
            href = a1.get('href')
            title = a1.find('h2').get_text()
            # print(href,title)

            svg = a.find('div','HotItem-metrics')
            heat = svg.get_text()[:-3]
            # print(title,href,heat)
            result['title'] = title
            result['href'] = href
            result['heat'] = heat
            # result.append(title)
            # result.append(href)
            # result.append(heat)
            # print(result)
            new_result = list(result.values())
            print(new_result)
            insert_info(new_result)
            # return new_result
            # result = {title}
            # print(svg)

def insert_info(result):
    sql = "INSERT INTO news(id,title,href,heat) VALUES (%s,%s,%s,%s)"
    print(sql)
    cursor.execute(sql,result)
    db.commit()


if __name__ == '__main__':
    url = "https://www.zhihu.com/hot"
    html = get_html(url)
    parse_page(html)
