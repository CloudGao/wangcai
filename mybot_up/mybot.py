# -*- coding:utf-8 -*-
import aiml
import commands
import Dialog
import speak
import listen
import time

from FM import FM
from Clock import Clock
from Joker import Joker
##from Weather import Weather

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

workers = []
workers.append(FM())
workers.append(Clock())
workers.append(Joker())
##workers.append(Weather())

statue = 'wait' #chat work wait

# Press CTRL-C to break this loop
while True:
    #waiting for wake up ,wake up then pause app
    if statue == 'wait' or statue == 'work' :
        wake_str = listen.listen()
        if wake_str == '旺财':
            speak.speak("小的在")
            statue = 'chat'
    
    
    #listening
    if statue == 'chat':
        input_str = listen.listen()
        respond_str = kernel.respond(input_str)
        #(status, output) = commands.getstatusoutput('espeak -vzh "'+ speak + '"')
        speak.speak(respond_str)
    
    #working ,no listen
    if statue == 'chat' :
        for w in workers:
            (result,out) = w.recever(respond_str)
            if result == False :
                continue
            #(status, output) = commands.getstatusoutput('espeak -vzh "'+ str(out) + '"')
            statue = 'work'
            #speak.speak(str(out))
            #out = ''
            #print out
    
    #ch
    if statue == 'chat':
        intent_code,results_text = Dialog.dialog(input_str)
        ##    commands.getstatusoutput('espeak -vzh "'+ str(results_text) + '"')
        if  str(results_text)=='如果你什么都不说，我也不知道怎么回答你呀' :
            statue = 'wait'
            continue
        else:
            speak.speak(str(results_text))
            print str(results_text)
    #print speak
    
    time.sleep(0.5)