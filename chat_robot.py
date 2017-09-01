# -*- coding:utf-8 -*-
import threading  # 多线程
import time
import itchat  # 主要库
import check_aria2
import weather
import bytime


itchat.auto_login()#enableCmdQR=-2,hotReload=True
#find the traget account by name,if you want to notice your self,then type your own nickname
users = itchat.search_friends(name="Lee's robot")
#find user by name
userName = users[0]['UserName']
#send message
def send_msg(msg):
    #use itchat API
    msg=msg.decode('utf-8')
    itchat.send(msg, userName)

#Push today and two more days' weather to your wechat
def push_weather():
    while 1:
        #get temperature information
        temperature=weather.get_temp()
        #get living index information
        life=weather.get_life()
        #send temperature information
        send_msg(temperature)
        time.sleep(1)
        #send living index information
        send_msg(life)
        #the parameter is the time you want it be sent to you tomorrow
        bytime.dosleep(9)

def push_download():
    check_aria2.init_list()
    while 1:
        time.sleep(60)
        msg,new_list=check_aria2.update_complete()
        check_aria2.complete_list=new_list
        if msg!='no':
            send_msg(msg)


t = threading.Thread(target=itchat.run)
t2 = threading.Thread(target=push_weather)
t3=threading.Thread(target=push_download)
t.start()
t2.start()
t3.start()
t.join()
t2.join()
t3.join()
