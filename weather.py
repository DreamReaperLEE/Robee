# -*- coding:utf-8 -*-

import urllib2, json

#get temperature information for three days
def get_temp():
    #use seniverse weather api,replace location with your city name
    c = urllib2.urlopen('https://api.seniverse.com/v3/weather/daily.json?key=nyxro3e5cgrffpmz&location=haerbin&language=zh-Hans&unit=c&start=0&days=3')
    #analysis the result,you can view the json format @ https://api.seniverse.com/
    result=json.loads(c.read())
    #get city name
    city=result['results'][0]['location']['name'].encode('utf-8')+'天气预报😐'
    #today's temperature information
    today_json=result['results'][0]['daily'][0]
    #tomorrows temperature information
    day2_json=result['results'][0]['daily'][1]
    #the day after tomorrow
    day3_json=result['results'][0]['daily'][2]
    #create detail message,I'm Chinese.so there are lots of chinese
    today = '今日白天:'+today_json['text_day'].encode('utf-8')+' 夜间：'+today_json['text_night'].encode('utf-8')+'\n最高气温：'+today_json['high'].encode('utf-8')+'℃ 最低气温：'+today_json['low'].encode('utf-8')+'℃'
    day2 = '明日白天:' + day2_json['text_day'].encode('utf-8') + ' 夜间：' + day2_json['text_night'].encode('utf-8') + '\n最高气温：' + day2_json['high'].encode('utf-8') + '℃ 最低气温：' + day2_json['low'].encode('utf-8') + '℃'
    day3 = '后日白天:' + day3_json['text_day'].encode('utf-8') + ' 夜间：' + day3_json['text_night'].encode('utf-8') + '\n最高气温：' + day3_json['high'].encode('utf-8') + '℃ 最低气温：' + day3_json['low'].encode('utf-8') + '℃'
    #combine all message in one message
    msg=city+'\n'+today+'\n'+'😱😱😱😱😱😱😱😱😱😱\n'+day2+'\n😱😱😱😱😱😱😱😱😱😱\n'+day3
    return msg


#get living index information
def get_life():
    #same as the past function
    c = urllib2.urlopen('https://api.seniverse.com/v3/life/suggestion.json?key=nyxro3e5cgrffpmz&location=haerbin&language=zh-Hans')
    result=json.loads(c.read())
    city=result['results'][0]['location']['name'].encode('utf-8')+'生活指数😐'
    suggest=result['results'][0]['suggestion']
    #travel index
    travel=suggest['travel']['brief'].encode('utf-8')
    #uv index
    uv=suggest['uv']['brief'].encode('utf-8')
    #flu index
    flu=suggest['flu']['brief'].encode('utf-8')
    #dressing index
    dressing=suggest['dressing']['brief'].encode('utf-8')
    #sport index
    sport=suggest['sport']['brief'].encode('utf-8')
    #combine them to together
    msg=city+'\n穿衣指数：\t'+dressing+'\n运动指数：\t'+sport+'\n紫外线指数:\t'+uv+'\n感冒指数：\t'+flu+'\n旅游指数：\t'+travel
    return msg