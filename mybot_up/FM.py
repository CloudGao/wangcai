# -*- coding:utf-8 -*-
from worker import worker
import commands

class FM(worker):
    
    def run(self):
        commands.getstatusoutput('mpc play 5')
        return None
    
    def pause(self):
        pass
        
    def stop(self):
        commands.getstatusoutput('mpc stop')
        return None
    
    def recever(self,responce):
        if responce == '好啊，正在打开收音机':
            self.run()
            return True,'别急'
        elif responce == '好啊，正在关上收音机':
            self.stop()
            return True,'别急'
        else:
            return False,None
    
