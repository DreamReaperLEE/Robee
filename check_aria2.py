# -*- coding:utf-8 -*-
import json
import urllib2

# download list
complete_list = []


# init the download list
def init_list():
    # params to get data,view aria2 jsonrpc api @ https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface
    jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'aria2.tellStopped', 'params': [0, 1000]})
    # send url request with post method
    c = urllib2.urlopen('http://45.77.101.40:6800/jsonrpc?tm=1504257059456', jsonreq)
    result = json.loads(c.read())
    # analysis the result
    result = result['result']
    # deal with the result in each row
    for every in result:
        # get file name
        name = every['files'][0]['path']
        if name == '':
            name = every['files'][0]['uris'][0]['uri']
        name = name.replace('/home/download/', '').encode('utf-8')
        # get file reason why it stop
        status = every['status'].encode('utf-8')
        # create message
        msg = '文件名：' + name + ' 状态：' + status
        # append new download into list
        complete_list.append(msg)


# check new download status
def update_complete():
    old_list = complete_list
    # init a new list
    new_list = []
    # same as the past function
    jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'aria2.tellStopped', 'params': [0, 1000]})
    c = urllib2.urlopen('http://45.77.101.40:6800/jsonrpc?tm=1504257059456', jsonreq)
    result = json.loads(c.read())
    result = result['result']
    for every in result:
        name = every['files'][0]['path']
        if name == '':
            name = every['files'][0]['uris'][0]['uri']
        name = name.replace('/home/download/', '').encode('utf-8')
        status = every['status'].encode('utf-8')
        msg = '文件名：' + name + '\n状态：' + status
        new_list.append(msg)
    msg = 'no'
    # if new list is different from the old one,then create trend message
    if list(set(new_list).difference(set(old_list))):
        more = list(set(new_list).difference(set(old_list)))
        msg = '下载有新动态:'
        for every in more:
            msg = msg + '\n' + every + '\n'
    return msg, new_list
