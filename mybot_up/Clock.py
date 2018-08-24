# -*- coding:utf-8 -*-
from worker import worker
import commands
from time import strftime,gmtime

class Clock(worker):
    
    def run(self):
        return str(strftime("%Y年%m月%d日 %H时%M分%S秒", gmtime()))
    
    def recever(self,responce):
        if responce == '我看看手表':
            str = '现在时间是:'+self.run()
            return True,str
        else:
            return False,None
        
