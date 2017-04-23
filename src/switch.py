#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def switch():
  SW1 = 21    # SW1 --> GPIO29(BCM:21,Physical:40)

  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # SW1を入力に設定、内部プルアップ抵抗を使用

  try:
    while True:
      state = GPIO.input(SW1)    # SW1の状態を読み込む(0:Low、1:High)
      print 'SW: %d' % state

      time.sleep(1)

  except KeyboardInterrupt:
    GPIO.cleanup()

if __name__ == "__main__":
  switch()
