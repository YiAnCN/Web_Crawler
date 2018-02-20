#爬取微博
import requests
import json
import time
from bs4 import BeautifulSoup

for page in range(1,11):
    print('---第',page,'页')
    url ='http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={}&pagebar=1&pl_name=Pl_Official_MyProfileFeed__22&id=1005052942550243&script_uri=/zhangqi8&feed_type=0&pre_page=7&domain_op=100505&__rnd=1506046330133'.format(page)
    cookie={'Cookie':'SINAGLOBAL=4968120555929.902.1504320931714; wvr=6; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; login_sid_t=88aa5ada11dc2b4edbc950c0bf2d4e27; YF-V5-G0=2da76c0c227d473404dd0efbaccd41ac; _s_tentry=-; UOR=,,www.google.co.jp; Apache=9801015550754.547.1506043269565; ULV=1506043269572:7:7:3:9801015550754.547.1506043269565:1505809545000; SSOLoginState=1506043276; SCF=Ai3dwKq7TX1KC7KsEdPv1-n3na0suMaxSjvSMgJKs0ixVwhpNAPh4jXTYHAD3ikkOgg_LTR6ClE0lQy-lztIXIU.; SUB=_2A250wBU7DeRhGeBO61AZ8SfFwjqIHXVXtAHzrDV8PUNbmtANLUalkW-Ces1wuVaUOQQ9qUjaMg_cSK2FZQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.BhLjxDKRM6NTEMCCLXvc5JpX5K2hUgL.Foq7ehzReK.41Kq2dJLoI0YLxKqL1hnL1KnLxK-L1-eLB.2LxKnL1K5L1-BLxKnL12-L1h.LxK-LB-BLBKeLxKqL1h.LB.qLxKML1K5L1-zt; SUHB=0YhR_q1pwuEFyZ; ALF=1537579276; un=15052967703; wb_cusLike_6002819996=N; YF-Page-G0=4c69ce1a525bc6d50f53626826cd2894'}
    
    r=requests.get(url,cookies=cookie)
    Data=json.loads(r.text)
    htmlstr=Data['data']        #重点，需要理解为什么

    soup=BeautifulSoup(htmlstr,'lxml')
    items=soup.find_all('div','WB_text W_f14')
    
    for item in items:
        item1=item.get_text().replace(' ','')
        print(item1)
    time.sleep(1)
    
    #将直接打印改为TXT文件保存的方法为：删去print(item1),改为：
        with open(r'C:\Users\Williams_Z\Desktop\movie4.txt','a+','encoding='utf-8') as f:
             f.write(item1)

                  
####################################################################################################################                 
#刘亦菲微博
                  
import requests
import json
from bs4 import BeautifulSoup

cookie={'Cookie':'SINAGLOBAL=4968120555929.902.1504320931714; login_sid_t=29c21dc1ed2a7110950e43cfea3903c7; cross_origin_proto=SSL; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=55fccf7be1706b6814a78384fa94e30c; _s_tentry=www.google.co.jp; UOR=,,www.google.co.jp; Apache=7777798574102.11.1508161737574; ULV=1508161737581:13:2:1:7777798574102.11.1508161737574:1507435876304; YF-Page-G0=416186e6974c7d5349e42861f3303251; SSOLoginState=1508162141; SCF=Ai3dwKq7TX1KC7KsEdPv1-n3na0suMaxSjvSMgJKs0ixu50jL3WMW4WSYb2nVWUGnAaYNdnJZ1Luwyx3ZwcGgpk.; SUB=_2A2504MoNDeRhGeBO61AZ8SfFwjqIHXVXl7zFrDV8PUNbmtANLRfAkW9h_9oYvL_Y5qfg_7bSxOZffJ3w6w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.BhLjxDKRM6NTEMCCLXvc5JpX5K2hUgL.Foq7ehzReK.41Kq2dJLoI0YLxKqL1hnL1KnLxK-L1-eLB.2LxKnL1K5L1-BLxKnL12-L1h.LxK-LB-BLBKeLxKqL1h.LB.qLxKML1K5L1-zt; SUHB=0y0Zsp7K46VF7j; ALF=1539698140; un=15052967703; wvr=6; wb_cusLike_6002819996=N; wb_cmtLike_6002819996=1'}
def get_url(url):
    r = requests.get(url,cookies=cookie)
    Data = json.loads(r.text)
    htmlstr = Data['data']
    return htmlstr

def parse_for_page(html):
    soup=BeautifulSoup(html,'lxml')
    divs=soup.find_all('div','WB_text W_f14')
    for div in divs:
        divss=div.get_text().replace(' ','')
    #   print(divss)
        with open(r'C:\Users\Williams_Z\Desktop\movie3.txt', 'a+', encoding='utf-8') as f:
            f.write(divss)


def main(page):
    url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100605&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__24&id=1006053261134763&script_uri=/liuyifeiofficial&feed_type=0&page={}&pre_page=1&domain_op=100605&__rnd=1508162492560'.format(page)
    html = get_url(url)
    parse_for_page(html)


if __name__ == '__main__':
    for page in range(1,11):
        main(page)
                  
                  

