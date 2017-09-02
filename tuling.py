# -*- coding:utf-8 -*-
import requests


# use tuling api to auto reply
def getTuling(msg):
    Url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '7fa204b3ea4e4db79c5b3072b5e65df2',
        'info': msg,
        'userid': 'reaper',
    }
    result = requests.post(Url, data=data).json()
    return result["text"]
