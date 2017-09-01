# -*- coding:utf-8 -*-
import urllib2, json


def get_complete():
    jsonreq = json.dumps({'jsonrpc':'2.0', 'id':1,
     'method':'aria2.tellStopped','params':[0,1000]})
    c = urllib2.urlopen('http://45.77.101.40:6800/jsonrpc?tm=1504257059456', jsonreq)
    result=json.loads(c.read())
    result=result['result']
    for every in result:
        name=every['files'][0]['path']
        if name=='':
            name=every['files'][0]['uris'][0]['uri']
        name=name.replace('/home/download/', '')
        ststus=every['status']
        print name
        print ststus