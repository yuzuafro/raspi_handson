#!/usr/bin/env python
# coding:utf-8

import webiopi

GPIO = webiopi.GPIO

RED   = 18

def setup():
    # GPIOをPWMに設定
    GPIO.setFunction(RED  , GPIO.PWM)

def destroy():
   # 消灯
    GPIO.pwmWrite(RED  , 0)
