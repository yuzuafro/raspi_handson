#! /usr/bin/env python
# coding:utf-8

import RPi.GPIO as GPIO
import time

if __name__ == ("__main__"):

  LED1 = 18    # LED1 --> GPIO1(BCM:18,Physical:12)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED1, GPIO.OUT)
  GPIO.output(LED1, GPIO.LOW)

  p18 = GPIO.PWM(LED1, 100)    # LED1の周波数設定(100Hz)
  p18.start(0)    # デューティ比 0 でPWM出力開始

  try:
    while 1:
      # 0〜100まで10段階でデューティ比を設定(プラス方向)
      for dc in range(0, 100, 10):
        p18.ChangeDutyCycle(dc)
        time.sleep(0.5)

      # 100〜0まで10段階でデューティ日を設定(マイナス方向)
      for dc in range(100, 0, -10):
        p18.ChangeDutyCycle(dc)
        time.sleep(0.5)

  except KeyboardInterrupt:
      print ('key interrupt')

  p18.stop()    # PWM出力を停止

  GPIO.cleanup()
