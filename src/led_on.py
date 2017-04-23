#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def led_on():
  LED1 = 18    # LED1 --> GPIO1(BCM:18,Physical:12)

  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(LED1, GPIO.OUT)    # LED1を出力に設定

  GPIO.output(LED1, GPIO.HIGH)    # ポートにHighの信号を出力(LEDが点灯します)
  time.sleep(2)

  GPIO.output(LED1, GPIO.LOW)    # ポートにLowの信号を出力(LEDが消灯します)

  GPIO.cleanup()

if __name__ == "__main__":
  led_on()
