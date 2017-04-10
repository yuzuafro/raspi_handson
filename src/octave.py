#! /usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

if __name__ == ("__main__"):

  BZ1 = 4    # BZ1 --> GPIO7
  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # GPIO7番を出力に設定

  tonename = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

  freq = 220.0    # 220Hz(低いラの音)
  buzzer = GPIO.PWM(BZ1, freq)
  buzzer.start(50)    # デューティ比 50 でPWM出力開始

  for i in range(0, 13):
    freq = 220.0 * (2 ** (i/12.0))
    print '%2s : %.1f Hz' % (tonename[i%12], freq)
    buzzer.ChangeFrequency(freq)    # 周波数を変更
    time.sleep(0.2)

  buzzer.stop()
  GPIO.cleanup()
