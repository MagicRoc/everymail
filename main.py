import threading
import time
from sendmail import send
def outosend():
    send()
    global t    #Notice: use global variable!
    t = threading.Timer(5.0, outosend)
    t.start()
t = threading.Timer(5.0, outosend)
while 1:
    if time.localtime()[4] == 47:
        t.start()
        break


