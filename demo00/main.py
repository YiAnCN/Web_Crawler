from demo00.mailTest import *
from demo00.newsTest import *

if __name__ == '__main__':
    url = "http://www.yangtse.com/"
    html = get_html(url)
    context = parse_page(html)
    send_email(context)



