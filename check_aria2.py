# -*- coding:utf-8 -*-
import urllib2, json
complete_list=[]

def init_list():
    jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 1,'method': 'aria2.tellStopped', 'params': [0, 1000]})
    c = urllib2.urlopen('http://45.77.101.40:6800/jsonrpc?tm=1504257059456', jsonreq)
    result = json.loads(c.read())
    result = result['result']
    for every in result:
        name = every['files'][0]['path']
        if name == '':
            name = every['files'][0]['uris'][0]['uri']
        name = name.replace('/home/download/', '').encode('utf-8')
        status = every['status'].encode('utf-8')
        msg='文件名：'+name+' 状态：'+status
        complete_list.append(msg)

def update_complete():
    old_list=complete_list
    new_list=[]
    jsonreq = json.dumps({'jsonrpc':'2.0', 'id':1,'method':'aria2.tellStopped','params':[0,1000]})
    c = urllib2.urlopen('http://45.77.101.40:6800/jsonrpc?tm=1504257059456', jsonreq)
    result=json.loads(c.read())
    result=result['result']
    for every in result:
        name=every['files'][0]['path']
        if name=='':
            name=every['files'][0]['uris'][0]['uri']
        name=name.replace('/home/download/', '').encode('utf-8')
        status=every['status'].encode('utf-8')
        msg='文件名：'+name+'\n状态：'+status
        new_list.append(msg)
    msg='no'
    if list(set(new_list).difference(set(old_list))):
        more = list(set(new_list).difference(set(old_list)))
        msg='下载有新动态:'
        for every in more:
            print every
            msg=msg+'\n'+every
    return msg,new_list