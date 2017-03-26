from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from weath import fetchWeather
from joke import fetchjoke
from word import fetchword
import smtplib

def _format_addr(s):
    """格式化一个邮件地址"""
	
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))





location = "河南南阳\n"
from_addr = '15518997683@163.com'
password = '******'   # 密钥
smtp_server = 'smtp.163.com' # 邮箱服务器



def send():

    jokeall = fetchjoke()

    jokeword = fetchword()
    jokeword = "\n\n\n单词：\n\n" + jokeword



    wea,weatime = fetchWeather()

    temp = "温度 : " + wea["temperature"] + "\n"
    weather = "天气 : " + wea["text"] + "\n"
    weatime = "天气更新时间 ：" + weatime + "\n\n\n"


    msg = MIMEText(location+temp+weather+weatime+jokeall+jokeword, 'plain','utf-8')
    msg['From'] = _format_addr('Everymail <%s>' % from_addr)
    msg['Subject'] = Header('The New day', 'utf-8').encode()

    with open("emails.txt","r") as f:
        emails = f.readlines()
	

    for to_addr in emails:
        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
