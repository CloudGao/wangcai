# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" ) 
import urllib2
import re
from bs4 import BeautifulSoup
from worker import worker


class Weather(worker):
    
    #定义获取天气数据函数
    def Get_weather_data(self):
        resp=urlopen('http://www.weather.com.cn/weather/101270101.shtml')
        soup=BeautifulSoup(resp,'html.parser')
        tagDate=soup.find('ul', class_="t clearfix")
        dates=tagDate.h1.string

        tagToday=soup.find('p', class_="tem")
        try:
            temperatureHigh=tagToday.span.string
        except AttributeError as e:
            temperatureHigh=tagToday.find_next('p', class_="tem").span.string

        temperatureLow=tagToday.i.string
        weather=soup.find('p', class_="wea").string

        tagWind=soup.find('p',class_="win")
        winL=tagWind.i.string
        return weather_dict
    #定义当天天气输出格式
    def Show_weather(self,weather_data):
        weather_dict = weather_data
        if weather_dict.get('desc') == 'invilad-citykey':
            print('你输入的城市有误或未收录天气，请重新输入...')
        elif weather_dict.get('desc') == 'OK':
            forecast = weather_dict.get('data').get('forecast')
            print('日期：', forecast[0].get('date'))
            print('城市：', weather_dict.get('data').get('city'))
            print('天气：', forecast[0].get('type'))
            print('温度：', weather_dict.get('data').get('wendu') + '℃ ')
            print('高温：', forecast[0].get('high'))
            print('低温：', forecast[0].get('low'))
            print('风级：', forecast[0].get('fengli').split('<')[2].split(']')[0])
            print('风向：', forecast[0].get('fengxiang'))
            weather_forecast_txt = '您好，您所在的城市%s,' \
                                   '天气%s,' \
                                   '当前温度%s，' \
                                   '今天最高温度%s，' \
                                   '最低温度%s，' \
                                   '风级%s，' \
                                   '温馨提示：%s' % \
                                   (
                                       weather_dict.get('data').get('city'),
                                       forecast[0].get('type'),
                                       weather_dict.get('data').get('wendu'),
                                       forecast[0].get('high'),
                                       forecast[0].get('low'),
                                       forecast[0].get('fengli').split('<')[2].split(']')[0],
                                       weather_dict.get('data').get('ganmao')
                                   )
            return weather_forecast_txt,forecast
        
    def run(self):
        weather_data = self.Get_weather_data()
        weather_forecast_txt, forecast = self.Show_weather(weather_data)
        return str(weather_forecast_txt)
    
    def recever(self,responce):
        if responce == '我夜观天象':
            str = self.run()
            return True,str
        else:
            return False,None