from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(text):
    user_mail = 'williams_z@yeah.net'
    password = '1175137542qq'
    send_mail = 'williams_z@139.com'
    smtp_server = 'smtp.yeah.net'

    #MIMEText 一共有三个参数：第一个参数为“邮件正文”；第二个参数指定“文本类型”，这里我们指定的是 plain，即文本信息；第三个参数为“正文编码”
    msg = MIMEText(text, 'plain', 'utf-8')
    #发件人姓名
    msg['From'] = _format_addr('扬子晚报头条新闻 <%s>' % user_mail)
    #收件人姓名
    msg['To'] = _format_addr('williams <%s>' % send_mail)
    #邮件标题
    msg['Subject'] = Header('新闻速递', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(user_mail, password)
    server.sendmail(user_mail, [send_mail], msg.as_string())
    server.quit()

