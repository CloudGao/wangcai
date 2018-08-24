# -*- coding:utf-8 -*-
import commands

print  commands.getstatusoutput('pocketsphinx_continuous -adcdev plughw:1,0 -nfft 2048 -samprate 48000')
