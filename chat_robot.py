# -*- coding:utf-8 -*-
import threading  # 多线程
import time

import itchat  # 主要库

import bytime
import check_aria2
import film
import weather

itchat.auto_login()  # enableCmdQR=True,hotReload=True
# find the traget account by name,if you want to notice your self,then type your own nickname
users = itchat.search_friends(name="Lee's robot")
# find user by name
userName = users[0]['UserName']


# send message
def send_msg(msg):
    # use itchat API
    msg = msg.decode('utf-8')
    itchat.send(msg, userName)


# Push today and two more days' weather to your wechat
def push_weather():
    while 1:
        # get temperature information
        temperature = weather.get_temp()
        # get living index information
        life = weather.get_life()
        # send temperature information
        send_msg(temperature)
        time.sleep(1)
        # send living index information
        send_msg(life)
        # the parameter is the time you want it be sent to you tomorrow
        bytime.dosleep(9)


# Push your download trends
def push_download():
    # init your download list
    check_aria2.complete_list = check_aria2.init_list()
    while 1:
        # check download list every 60 seconds
        time.sleep(60)
        # get trend message and new download list
        msg, new_list = check_aria2.update_complete()
        # replace download list by a new list
        check_aria2.complete_list = new_list
        # if the msg is not 'no' then it means got new trends
        if msg != 'no':
            send_msg(msg)


# Push  film trends
def push_film():
    # init your film list
    msg, film.film_list = film.get_film_list()
    while 1:
        # get trend film and new film list
        msg, new_list = film.get_film_list()
        # replace film list by a new list
        film.film_list = new_list
        # if the msg is not 'no' then it means got new trends
        if msg != 'no':
            send_msg(msg)
        # check film list every 60 seconds
        time.sleep(3600)


# creat thread
t = threading.Thread(target=itchat.run)
t2 = threading.Thread(target=push_weather)
t3 = threading.Thread(target=push_download)
t4 = threading.Thread(target=push_film)
t.start()
t2.start()
t3.start()
t4.start()
t.join()
t2.join()
t3.join()
t4.join()
