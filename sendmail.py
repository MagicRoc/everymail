from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from weath import fetchWeather
import smtplib

def _format_addr(s):
    """格式化一个邮件地址"""
	
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

wea,weatime = fetchWeather()
temp = "温度 : " + wea["temperature"] + "\n"
weather = "天气 : " + wea["text"] + "\n"
weatime = "天气更新时间 ：" + weatime + "\n"
from_addr = '15518997683@163.com'
password = 'asd123456'   # 密钥
to_addr = '917086506@qq.com' 
smtp_server = 'smtp.163.com' # 邮箱服务器

msg = MIMEText(temp+weather+weatime+'hello, everymail', 'plain', 'utf-8')
msg['From'] = _format_addr('Everymail <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('The New day', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
