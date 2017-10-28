import os
from PIL import Image

def download_pic(html):
    soup = BeautifulSoup(html, 'lxml')
    picture = soup.find('dl', {'style': 'POSITION: relative'}).find('dd')
    pic='http://jweb.cucn.edu.cn/' + picture.find('img').attrs['src']
    r=requests.get(pic)
    with open('pic.png','wb') as f:
        f.write(r.content)
    # return pic

def open_pic():
    image=Image.open('{}/pic.png'.format(os.getcwd()))
    image.show()
