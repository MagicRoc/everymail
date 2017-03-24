import threading
import time
from sendmail import send
def outosend():
    """自动发送邮件，递归实现"""
    send()
    global t    #Notice: use global variable!
    t = threading.Timer(8.0, outosend)    # 定时器
    t.start()
t = threading.Timer(5.0, outosend)
while 1:
    if time.localtime()[3] == 6:  # 判断现在是不是早晨六点
        t.start()   
        break     # 线程不能重复开始，不然会有警告


