# coding:utf-8

import urllib2

# 引入相关模块
from bs4 import BeautifulSoup

# film list
film_list = []


# get new film list and trends
def get_film_list():
    old_list = film_list
    new_list = []
    url = "http://www.hao6v.com/"
    response = urllib2.urlopen(url)
    wbdata = response.read()
    # analysis the text that you got
    soup = BeautifulSoup(wbdata, 'lxml')
    # select specific element
    news_titles = soup.select("body > div#main > div.col2 > div.box > ul.lt > li > a")
    # ergodic the list
    i = 1
    for n in news_titles:
        if i == 18:
            break
        # get title
        title = n.get_text().encode('utf-8')
        new_list.append(title)
        i = i + 1
    msg = 'no'
    # if new list is different from the old one,then create trend message
    if list(set(new_list).difference(set(old_list))):
        more = list(set(new_list).difference(set(old_list)))
        msg = '6V新电影:'
        for every in more:
            msg = msg + '\n' + every + '\n'
    return msg, new_list
