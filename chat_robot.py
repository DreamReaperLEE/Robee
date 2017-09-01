# -*- coding:utf-8 -*-
import threading  # 多线程
import time
import itchat  # 主要库

itchat.auto_login()#enableCmdQR=-2,hotReload=True
#想给谁发信息，先查找到这个朋友
users = itchat.search_friends(name="Lee's robot")
#找到UserName
userName = users[0]['UserName']
def send_msg():
    itchat.send('hello @Sumail Lee', userName)

def wait():
    while 1:
        time.sleep(5)
        send_msg()


t = threading.Thread(target=itchat.run)
t2 = threading.Thread(target=wait)
t.start()
t2.start()
t.join()
t2.join()
