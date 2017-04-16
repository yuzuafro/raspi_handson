#! /usr/bin/env python
# coding:utf-8

import RPi.GPIO as GPIO
import time

if __name__ == ("__main__"):

  BZ1 = 4    # BZ1 --> GPIO7(BCM:4,Physical:7)

  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # BZ1を出力に設定
  buzzer = GPIO.PWM(BZ1, 440)    # BZ1の周波数設定(440Hz)

  buzzer.start(50)    # デューティ比 50 でPWM出力開始

  time.sleep(1)

  buzzer.stop()    # PWM出力を停止

  GPIO.cleanup()    # GPIOポートの撤収処理
