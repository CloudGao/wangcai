#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import time
import urllib
import json
import hashlib
import base64
import commands

def record():
    print commands.getstatusoutput('sudo arecord -D "plughw:1,0" -d 5 audio/listen_temp.wav -r 16000')
    print commands.getstatusoutput('sox audio/listen_temp.wav -r 16000 -b 16 audio/listen_temp2.wav')

def listen():
    record()
    f = open("audio/listen_temp2.wav", 'rb')
    file_content = f.read()
    base64_audio = base64.b64encode(file_content)
    body = urllib.urlencode({'audio': base64_audio})

    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    api_key = ''
    param = {"engine_type": "sms16k", "aue": "raw","scene": "main"}

    x_appid = ''
    x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5(api_key + str(x_time) + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib2.Request(url, body, x_header)
    result = urllib2.urlopen(req)
    result = result.read()
    str2 = json.loads(result)['data']
    print result
    return str2.strip('。，？！')
