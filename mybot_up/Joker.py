# -*- coding:utf-8 -*-
from worker import worker
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" ) 
import random

class Joker(worker):
    
    def run(self):
        rule_joke=re.compile('<span id=\"text110\">([\w\W]*?)</span>')
        rule_url=re.compile('<a href=\"(.*?)\"target=\"_blank\" >')
        mainUrl='http://www.jokeji.cn'
        url='http://www.jokeji.cn/list.htm'
         
        req=urllib2.urlopen(url)
        html=req.read().decode('gbk')
        urls=rule_url.findall(html)
        for i in range(4):
                url2=urllib2.quote(urls[i])
                joke_url=mainUrl+url2
                req2=urllib2.urlopen(joke_url)
                html2=req2.read().decode('gbk')
                joke=rule_joke.findall(html2)
                jokes=joke[0].split('<P>')
                
        str=jokes[random.randint(0,len(jokes)-1)].replace('</P>','')
	str=str.replace('<BR>','')
	
	str=str[2:]
        return str
    
    def recever(self,responce):
        if responce == '我打开我的小本本':
            str = self.run()
            return True,str
        else:
            return False,None
    
